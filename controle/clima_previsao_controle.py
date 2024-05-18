from entidade.clima_previsao_entidade import ClimaPrevisaoEntidade
from limite.clima_previsao_tela import ClimaPrevisaoTela


class ClimaPrevisaoControle:
    def __init__(self):
        self.__log_previsao = []
        self.__clima_previsao_tela = ClimaPrevisaoTela()
