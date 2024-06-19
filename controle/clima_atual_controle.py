from entidade.clima_atual import ClimaAtual
from limite.clima_atual_tela import ClimaAtualTela
from controle.clima_controle_abstrato import ClimaControleAbstrato
from datetime import datetime
from entidade.localizacao import Localizacao


class ClimaAtualControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__log = []
        self.__climas_atuais = []
        self.__clima_atual_tela = ClimaAtualTela()

    def ver_dados_climaticos(self):
        self.__sistema.controlador_usuario.listar_usuarios()
        self.__sistema.controlador_localizacao.listar_localizacoes()
        dados = self.__clima_atual_tela.pega_dados_ver_clima()
        usuario = self.__sistema.controlador_usuario.procurar_usuario_por_cpf(dados["cpf"])
        localizacao = self.__sistema.controlador_localizacao.procura_localizacao_por_cidade(dados["cidade"])
        if usuario is not None and localizacao is not None:
            clima = self.procura_clima_atual_por_localizacao(localizacao)
            if clima is None:
                clima = ClimaAtual(usuario, localizacao)
                self.__climas_atuais.append(clima)
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

    '''
    #quando apagar o log apagar do lista climas tambem
    def remove_clima_atual(self, clima_atual: ClimaAtual):
        if clima_atual in self.__climas_atuais:
            self.__climas_atuais.remove(clima_atual)
    '''

    def procura_clima_atual_por_localizacao(self, localizacao: Localizacao):
        if isinstance(localizacao, Localizacao):
            for clima_atual in self.__climas_atuais:
                if clima_atual.localizacao == localizacao:
                    return clima_atual
            return None

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

    def temperatura_mais_baixa(self):
        min_temperatura = 56
        for clima_atual in self.__climas_atuais:
            temperatura = clima_atual.temperatura
            if temperatura <= min_temperatura:
                min_temperatura = temperatura
                cidade_temperatura_mais_baixa = clima_atual.localizacao.cidade
        self.__clima_atual_tela.mostra_temperatura_mais_baixa(min_temperatura, cidade_temperatura_mais_baixa)

    def temperatura_mais_alta(self):
        max_temperatura = -67
        for clima_atual in self.__climas_atuais:
            temperatura = clima_atual.temperatura
            if temperatura >= max_temperatura:
                max_temperatura = temperatura
                cidade_temperatura_mais_alta = clima_atual.localizacao.cidade
        self.__clima_atual_tela.mostra_temperatura_mais_alta(max_temperatura, cidade_temperatura_mais_alta)

    def abre_tela(self):
        lista_opcoes = {1: self.ver_dados_climaticos, 2: self.lista_log,
                        3: self.apaga_log, 4: self.apaga_log_especifico,
                        5: self.temperatura_mais_alta, 6: self.temperatura_mais_baixa, 0: self.retornar}

        while True:
            opcao_escolhida = self.__clima_atual_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
