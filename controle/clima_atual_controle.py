from entidade.clima_atual_entidade import ClimaAtualEntidade
from limite.clima_atual_tela import ClimaAtualTela
from controle.clima_controle_abstrato import ClimaControleAbstrato


class ClimaAtualControle(ClimaControleAbstrato):
    def __init__(self, sistema):
        super().__init__(sistema)
        self.__log = []
        self.__clima_atual_tela = ClimaAtualTela()

    def ver_dados_climaticos(self):
        pass

    def adiciona_log(self):
        pass

    def lista_log(self):
        pass

    def apaga_log(self):
        pass

    def apaga_log_especifico(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.ver_dados_climaticos, 2: self.lista_log,
                        3: self.apaga_log, 4: self.apaga_log_especifico,
                        0: self.retornar}