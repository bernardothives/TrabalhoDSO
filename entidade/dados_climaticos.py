from random import randint


class DadosClimaticos:
    def __init__(self):
        pass

    @staticmethod
    def pega_temperatura():
        return randint(-67, 56)

    @staticmethod
    def pega_humidade():
        return randint(0, 100)

    @staticmethod
    def pega_velocidade_vento():
        return randint(0, 408)

    @staticmethod
    def pega_volume_chuva():
        return randint(0, 1825)

    @staticmethod
    def pega_visibilidade():
        return randint(0, 100)

    @staticmethod
    def pega_sensacao_termica():
        return randint(-67, 56)
