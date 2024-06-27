from DAOs.dao import DAO
from entidade.localizacao import Localizacao


class LocalizacaoDAO(DAO):
    def __init__(self):
        super().__init__('localizacao.pkl')

    def add(self, localizacao: Localizacao):
        if localizacao is not None and isinstance(localizacao, Localizacao) and localizacao.cidade is not None:
            super().add(localizacao.cidade, localizacao)

    def update(self, localizacao: Localizacao):
        if localizacao is not None and isinstance(localizacao, Localizacao) and localizacao.cidade is not None:
            super().update(localizacao.cidade, localizacao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
