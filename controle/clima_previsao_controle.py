from entidade.clima_previsao_entidade import ClimaPrevisaoEntidade
from limite.clima_previsao_tela import ClimaPrevisaoTela
from controle.clima_controle_abstrato import ClimaControleAbstrato


class ClimaPrevisaoControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__log = []
        self.__clima_previsao_tela = ClimaPrevisaoTela()

    def abre_tela(self):
        pass

    def adiciona_log(self):
        pass

    def apaga_log(self):
        pass

    def apaga_log_especifico(self):
        pass

    def lista_log(self):
        pass

    def ver_dados_climaticos(self):
        pass
