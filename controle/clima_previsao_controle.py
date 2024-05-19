from entidade.clima_previsao_entidade import ClimaPrevisaoEntidade
from limite.clima_previsao_tela import ClimaPrevisaoTela
from controle.clima_controle_abstrato import ClimaControleAbstrato


class ClimaPrevisaoControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__log = []
        self.__clima_previsao_tela = ClimaPrevisaoTela()

    def ver_dados_climaticos(self):
        pass

    def procura_log_por_cpf(self):
        pass

    def adiciona_log(self):
        pass

    def lista_log(self):
        pass

    def apaga_log(self):
        pass

    def apaga_log_especifico(self):
        pass

    def abre_tela(self): #arrumar certo p esse
        lista_opcoes = {1: self.ver_dados_climaticos, 2: self.lista_log,
                        3: self.apaga_log, 4: self.apaga_log_especifico,
                        0: self.retornar}
