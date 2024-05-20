from abc import ABC, abstractmethod


class ClimaControleAbstrato(ABC):
    @abstractmethod
    def __init__(self, sistema):
        self.__sistema = sistema

    @abstractmethod
    def procura_log_por_cpf(self, cpf: str):
        pass

    @abstractmethod
    def ver_dados_climaticos(self):
        pass

    @abstractmethod
    def adiciona_log(self, cpf: str, cidade: str):
        pass

    @abstractmethod
    def lista_log(self):
        pass

    @abstractmethod
    def apaga_log(self):
        pass

    @abstractmethod
    def apaga_log_especifico(self):
        pass

    @abstractmethod
    def abre_tela(self):
        pass

    @abstractmethod
    def retornar(self):
        pass
