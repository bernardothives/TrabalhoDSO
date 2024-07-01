from abc import ABC, abstractmethod
from entidade.dados_climaticos import DadosClimaticos
from entidade.usuario import Usuario
from entidade.localizacao import Localizacao
from datetime import datetime
import random


class ClimaAbstrato(ABC):
    @abstractmethod
    def __init__(self, usuario: Usuario, localizacao: Localizacao):
        self.__id = str(random.randint(100000, 999999))
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
        if isinstance(localizacao, Localizacao):
            self.__localizacao = localizacao
        self.dados_climaticos = DadosClimaticos()
        self.__temperatura = self.dados_climaticos.pega_temperatura()
        self.__humidade = self.dados_climaticos.pega_humidade()
        self.__velocidade_vento = self.dados_climaticos.pega_velocidade_vento()
        self.__volume_chuva = self.dados_climaticos.pega_volume_chuva()
        self.__visibilidade = self.dados_climaticos.pega_visibilidade()
        self.__sensacao_termica = self.dados_climaticos.pega_sensacao_termica()
        self.__data = datetime.now().strftime('%d/%m/%Y')

    @property
    def id(self):
        return self.__id

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario

    @property
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao: Localizacao):
        if isinstance(localizacao, Localizacao):
            self.__localizacao = localizacao

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

    @data.setter
    def data(self, data: str):
        self.__data = data
