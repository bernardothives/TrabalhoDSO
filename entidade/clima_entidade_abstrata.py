from abc import ABC, abstractmethod


class ClimaEntidadeAbstrata(ABC):
    @abstractmethod
    def __init__(self, temperatura: int, humidade: int,
                 velocidade_vento: int, volume_chuva: int,
                 visibilidade: int, sensacao_termica: int, data: str):
        if isinstance(temperatura, int):
            self.__temperatura = temperatura
        if isinstance(humidade, int):
            self.__humidade = humidade
        if isinstance(velocidade_vento, int):
            self.__velocidade_vento = velocidade_vento
        if isinstance(volume_chuva, int):
            self.__volume_chuva = volume_chuva
        if isinstance(visibilidade, int):
            self.__visibilidade = visibilidade
        if isinstance(sensacao_termica, int):
            self.__sensacao_termica = sensacao_termica
        if isinstance(data, str):
            self.__data = data

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura: int):
        if isinstance(temperatura, int):
            self.__temperatura = temperatura

    @property
    def humidade(self):
        return self.__humidade

    @humidade.setter
    def humidade(self, humidade: int):
        if isinstance(humidade, int):
            self.__humidade = humidade

    @property
    def velocidade_vento(self):
        return self.__velocidade_vento

    @velocidade_vento.setter
    def velocidade_vento(self, velocidade_vento: int):
        if isinstance(velocidade_vento, int):
            self.__velocidade_vento = velocidade_vento

    @property
    def volume_chuva(self):
        return self.__volume_chuva

    @volume_chuva.setter
    def volume_chuva(self, volume_chuva: int):
        if isinstance(volume_chuva, int):
            self.__volume_chuva = volume_chuva

    @property
    def visibilidade(self):
        return self.__visibilidade

    @visibilidade.setter
    def visibilidade(self, visibilidade: int):
        if isinstance(visibilidade, int):
            self.__visibilidade = visibilidade

    @property
    def sensacao_termica(self):
        return self.__sensacao_termica

    @sensacao_termica.setter
    def sensacao_termica(self, sensacao_termica: int):
        if isinstance(sensacao_termica, int):
            self.__sensacao_termica = sensacao_termica

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data
