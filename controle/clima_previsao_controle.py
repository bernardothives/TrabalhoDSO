from entidade.clima_previsao_entidade import ClimaPrevisaoEntidade
from limite.clima_previsao_tela import ClimaPrevisaoTela
from controle.clima_controle_abstrato import ClimaControleAbstrato
from controle.alerta_controle import AlertaControle
from datetime import datetime


class ClimaPrevisaoControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__log = []
        self.__clima_previsao_tela = ClimaPrevisaoTela()
        self.__controlador_alerta = AlertaControle(self)

    def ver_dados_climaticos(self):
        self.__sistema.controlador_usuario.listar_usuarios()
        self.__sistema.controlador_localizacao.listar_localizacoes()
        dados = self.__clima_previsao_tela.pega_dados_ver_clima()
        usuario = self.__sistema.controlador_usuario.procurar_usuario_por_cpf(dados["cpf"])
        localizacao = self.__sistema.controlador_localizacao.procura_localizacao_por_cidade(dados["cidade"])
        if usuario is not None and localizacao is not None:
            clima = ClimaPrevisaoEntidade(usuario, localizacao)
            self.adiciona_log()
            self.__clima_previsao_tela.mostra_clima({"temperatura": clima.temperatura,
                                                     "humidade": clima.humidade,
                                                     "velocidade_vento": clima.velocidade_vento,
                                                     "volume_chuva": clima.volume_chuva,
                                                     "visibilidade": clima.visibilidade,
                                                     "sensacao_termica": clima.sensacao_termica,
                                                     "data": clima.data,
                                                     "descricao": clima.descricao})
        else:
            self.__clima_previsao_tela.mostra_msg("Dados Invalidos")

    def procura_log_por_cpf(self, cpf: str):
        logs_do_cpf = []
        for log in self.__log:
            if log[0] == cpf:
                logs_do_cpf.append(log)
            return logs_do_cpf
        return None

    def adiciona_log(self):
        dados = self.__clima_previsao_tela.pega_dados_ver_clima()
        hora = datetime.now().strftime('%H:%M:%S')
        self.__log.append([dados["cpf"], dados["cidade"], hora])

    def lista_log(self):
        for log in self.__log:
            self.__clima_previsao_tela.mostra_log({"cpf": log[0],
                                                   "cidade": log[1],
                                                   "hora": log[2]})

    def apaga_log(self):
        self.__log.clear()

    def apaga_log_especifico(self):
        self.lista_log()
        cpf = self.__clima_previsao_tela.seleciona_cpf()
        logs = self.procura_log_por_cpf(cpf)
        if logs is not None:
            for log in logs:
                self.__log.remove(log)
            self.lista_log()
        else:
            self.__clima_previsao_tela.mostra_msg("ATENÇÂO: Este cpf nao possui logs")

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_dados_climaticos, 2: self.lista_log,
                        3: self.apaga_log, 4: self.apaga_log_especifico,
                        5: self.opcoes_alerta, 0: self.retornar}

        while True:
            opcao_escolhida = self.__clima_previsao_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def opcoes_alerta(self):
        self.__controlador_alerta.abre_tela()
