from entidade.clima_atual_entidade import ClimaAtualEntidade
from limite.clima_atual_tela import ClimaAtualTela


class ClimaAtualControle:
    def __init__(self):
        self.__log_atual = []
        self.__clima_atual_tela = ClimaAtualTela()
