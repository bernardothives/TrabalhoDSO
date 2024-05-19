from abc import ABC, abstractmethod
from entidade.dados_climaticos import DadosClimaticos
from datetime import datetime


class ClimaEntidadeAbstrata(ABC):
    @abstractmethod
    def __init__(self, temperatura: int, humidade: int,
                 velocidade_vento: int, volume_chuva: int,
                 visibilidade: int, sensacao_termica: int, data: str):
        self.dados_climaticos = DadosClimaticos()
        self.__temperatura = self.dados_climaticos.pega_temperatura()
        self.__humidade = self.dados_climaticos.pega_humidade()
        self.__velocidade_vento = self.dados_climaticos.pega_velocidade_vento()
        self.__volume_chuva = self.dados_climaticos.pega_volume_chuva()
        self.__visibilidade = self.dados_climaticos.pega_visibilidade()
        self.__sensacao_termica = self.dados_climaticos.pega_sensacao_termica()
        if isinstance(data, str):
            self.__data = data  #fazer com o date time

    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def humidade(self):
        return self.__humidade

    @property
    def velocidade_vento(self):
        return self.__velocidade_vento

    @property
    def volume_chuva(self):
        return self.__volume_chuva

    @property
    def visibilidade(self):
        return self.__visibilidade

    @property
    def sensacao_termica(self):
        return self.__sensacao_termica

    @property
    def data(self):
        return self.__data
