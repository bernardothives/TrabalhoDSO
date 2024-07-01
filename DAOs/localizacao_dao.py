from DAOs.dao import DAO
from entidade.localizacao import Localizacao


class LocalizacaoDAO(DAO):
    def __init__(self):
        super().__init__('localizacao.pkl')

    def add(self, localizacao: Localizacao):
        if localizacao is not None and isinstance(localizacao, Localizacao) and isinstance(localizacao.cidade, str):
            super().add(localizacao.cidade, localizacao)

    def update(self, localizacao: Localizacao):
        if localizacao is not None and isinstance(localizacao, Localizacao) and isinstance(localizacao.cidade, str):
            super().update(localizacao.cidade, localizacao)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

