from random import randint


class DadosClimaticos:
    def __init__(self):
        pass

    def pega_temperatura(self):
        return randint(-67, 56)

    def pega_humidade(self):
        return randint(0, 100)

    def pega_velocidade_vento(self):
        return randint(0, 408)

    def pega_volume_chuva(self):
        return randint(0, 1825)

    def pega_visibilidade(self):
        return randint(0, 100)

    def pega_sensacao_termica(self):
        return randint(-67, 56)
