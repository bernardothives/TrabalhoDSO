from entidade.clima_previsao import ClimaPrevisao
from limite.clima_previsao_tela import ClimaPrevisaoTela
from controle.clima_controle_abstrato import ClimaControleAbstrato
from controle.alerta_controle import AlertaControle
from entidade.localizacao import Localizacao
from datetime import datetime, timedelta
from DAOs.clima_previsao_dao import ClimaPrevisaoDAO
from entidade.usuario import Usuario


class ClimaPrevisaoControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__log = []
        self.__previsoes_DAO = ClimaPrevisaoDAO()
        self.__clima_previsao_tela = ClimaPrevisaoTela()
        self.__controlador_alerta = AlertaControle(self)

    @property
    def sistema(self):
        return self.__sistema

    def ver_dados_climaticos(self):
        self.__sistema.controlador_usuario.listar_usuarios()
        self.__sistema.controlador_localizacao.listar_localizacoes()
        dados = self.__clima_previsao_tela.pega_dados_ver_clima()
        if dados:
            usuario = self.__sistema.controlador_usuario.procurar_usuario_por_cpf(dados["cpf"])
            localizacao = self.__sistema.controlador_localizacao.procura_localizacao_por_cidade(dados["cidade"])
            if usuario and localizacao:
                clima_id = self.procura_id_clima_previsao_por_usuario_e_localizacao(usuario, localizacao)
                clima = self.procura_clima_previsao_por_id(clima_id)
                if clima is None:
                    clima = ClimaPrevisao(usuario, localizacao)
                    self.__previsoes_DAO.add(clima)
                if isinstance(clima.data, datetime):
                    data_str = clima.data.strftime('%d/%m/%Y')
                else:
                    data_str = clima.data
                clima.data = datetime.strptime(data_str, '%d/%m/%Y')
                data_previsao = clima.data + timedelta(days=1)
                data_formatada = data_previsao.strftime('%d/%m/%Y')
                self.adiciona_log(dados["cpf"], dados["cidade"])
                self.__clima_previsao_tela.mostra_clima({"temperatura": clima.temperatura,
                                                         "humidade": clima.humidade,
                                                         "velocidade_vento": clima.velocidade_vento,
                                                         "volume_chuva": clima.volume_chuva,
                                                         "visibilidade": clima.visibilidade,
                                                         "sensacao_termica": clima.sensacao_termica,
                                                         "data": data_formatada})
            else:
                self.__clima_previsao_tela.mostra_msg("Dados Invalidos")

    def procura_id_clima_previsao_por_usuario_e_localizacao(self, usuario: Usuario, localizacao: Localizacao):
        for clima_previsao in self.__previsoes_DAO.get_all():
            if clima_previsao.usuario == usuario and clima_previsao.localizacao == localizacao:
                return clima_previsao.id
        return None

    def procura_id_clima_previsao_por_localizacao(self, localizacao: Localizacao):
        for clima_previsao in self.__previsoes_DAO.get_all():
            if clima_previsao.localizacao == localizacao:
                return clima_previsao.id
        return None

    def procura_clima_previsao_por_id(self, id):
        return self.__previsoes_DAO.get(id)

    def procura_log_por_cpf(self, cpf: str):
        logs_do_cpf = []
        for log in self.__log:
            if log[0] == cpf:
                logs_do_cpf.append(log)
        if logs_do_cpf:
            return logs_do_cpf
        else:
            return None

    def adiciona_log(self, cpf: str, cidade: str):
        hora = datetime.now().strftime('%H:%M:%S')
        self.__log.append([cpf, cidade, hora])

    def lista_log(self):
        if self.__log:
            for log in self.__log:
                self.__clima_previsao_tela.mostra_log({"cpf": log[0],
                                                    "cidade": log[1],
                                                    "hora": log[2]})
        else:
            self.__clima_previsao_tela.mostra_msg("Nenhum registro de atividade foi encontrado")

    def apaga_log(self):
        for log in self.__log:
            cpf = log[0]
            cidade = log[1]
            usuario = self.__sistema.controlador_usuario.procurar_usuario_por_cpf(cpf)
            localizacao = self.__sistema.controlador_localizacao.procura_localizacao_por_cidade(cidade)
            if usuario and localizacao:
                clima_id = self.procura_id_clima_previsao_por_usuario_e_localizacao(usuario, localizacao)
                if clima_id:
                    self.__previsoes_DAO.remove(clima_id)
        self.__log.clear()

    def apaga_log_especifico(self):
        self.lista_log()
        cpf = self.__clima_previsao_tela.seleciona_cpf()
        logs = self.procura_log_por_cpf(cpf)
        if logs is not None:
            for log in logs:
                self.__log.remove(log)
                cidade = log[1]
                usuario = self.__sistema.controlador_usuario.procurar_usuario_por_cpf(cpf)
                localizacao = self.__sistema.controlador_localizacao.procura_localizacao_por_cidade(cidade)
                if usuario and localizacao:
                    clima_id = self.procura_id_clima_previsao_por_usuario_e_localizacao(usuario, localizacao)
                    if clima_id:
                        self.__previsoes_DAO.remove(clima_id)
            self.lista_log()
        else:
            self.__clima_previsao_tela.mostra_msg("ATENÇÃO: Este cpf não possui logs")

    def retornar(self):
        self.__sistema.abre_tela()

    def remove_clima_previsao(self):
        self.listar_climas_previsao()
        clima_id = self.__clima_previsao_tela.seleciona_id()
        if clima_id is not None:
            self.__previsoes_DAO.remove(clima_id)
            self.__clima_previsao_tela.mostra_msg("removido com sucesso!")

    def listar_climas_previsao(self):
        climas_previsoes = self.__previsoes_DAO.get_all()
        if not climas_previsoes:
            self.__clima_previsao_tela.mostra_msg("Nenhum clima cadastrado")
        else:
            for clima_previsao in climas_previsoes:
                dado_clima_previsao = {
                    'cpf': clima_previsao.usuario.cpf,
                    'cidade': clima_previsao.localizacao.cidade,
                    'id': clima_previsao.id
                }
                self.__clima_previsao_tela.mostra_dados_clima(dado_clima_previsao)

    def abre_tela(self):
        lista_opcoes = {1: self.ver_dados_climaticos, 2: self.lista_log,
                        3: self.apaga_log, 4: self.apaga_log_especifico,
                        5: self.opcoes_alerta, 6: self.remove_clima_previsao,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__clima_previsao_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def opcoes_alerta(self):
        self.__controlador_alerta.abre_tela()
