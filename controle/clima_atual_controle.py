from entidade.clima_atual_entidade import ClimaAtualEntidade
from limite.clima_atual_tela import ClimaAtualTela
from controle.clima_controle_abstrato import ClimaControleAbstrato
from datetime import datetime


class ClimaAtualControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__log = []
        self.__clima_atual_tela = ClimaAtualTela()

    def ver_dados_climaticos(self):
        self.__sistema.controlador_usuario.listar_usuarios()
        self.__sistema.controlador_localizacao.listar_localizacoes()
        dados = self.__clima_atual_tela.pega_dados_ver_clima()
        usuario = self.__sistema.controlador_usuario.procurar_usuario_por_cpf(dados["cpf"])
        localizacao = self.__sistema.controlador_localizacao.procura_localizacao_por_cidade(dados["cidade"])
        if usuario is not None and localizacao is not None:
            clima = ClimaAtualEntidade(usuario, localizacao)
            self.adiciona_log(dados["cpf"], dados["cidade"])
            self.__clima_atual_tela.mostra_clima({"temperatura": clima.temperatura,
                                                  "humidade": clima.humidade,
                                                  "velocidade_vento": clima.velocidade_vento,
                                                  "volume_chuva": clima.volume_chuva,
                                                  "visibilidade": clima.visibilidade,
                                                  "sensacao_termica": clima.sensacao_termica,
                                                  "data": clima.data,
                                                  "horario": clima.horario})
        else:
            self.__clima_atual_tela.mostra_msg("Dados Invalidos")

    def procura_log_por_cpf(self, cpf: str):
        logs_do_cpf = []
        for log in self.__log:
            if log[0] == cpf:
                logs_do_cpf.append(log)
            return logs_do_cpf
        return None

    def adiciona_log(self, cpf: str, cidade: str):
        hora = datetime.now().strftime('%H:%M:%S')
        self.__log.append([cpf, cidade, hora])

    def lista_log(self):
        for log in self.__log:
            self.__clima_atual_tela.mostra_log({"cpf": log[0],
                                                "cidade": log[1],
                                                "hora": log[2]})

    def apaga_log(self):
        self.__log.clear()

    def apaga_log_especifico(self):
        self.lista_log()
        cpf = self.__clima_atual_tela.seleciona_cpf()
        logs = self.procura_log_por_cpf(cpf)
        if logs is not None:
            for log in logs:
                self.__log.remove(log)
            self.lista_log()
        else:
            self.__clima_atual_tela.mostra_msg("ATENÇÂO: Este cpf nao possui logs")

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_dados_climaticos, 2: self.lista_log,
                        3: self.apaga_log, 4: self.apaga_log_especifico,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__clima_atual_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
