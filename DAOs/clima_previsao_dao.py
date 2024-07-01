from DAOs.dao import DAO
from entidade.clima_previsao import ClimaPrevisao


class ClimaPrevisaoDAO(DAO):
    def __init__(self):
        super().__init__('clima_previsao.pkl')

    def add(self, clima_previsao: ClimaPrevisao):
        if (clima_previsao is not None and isinstance(clima_previsao, ClimaPrevisao)
                and isinstance(clima_previsao.id, str)):
            super().add(clima_previsao.id, clima_previsao)

    def update(self, clima_previsao: ClimaPrevisao):
        if (clima_previsao is not None and isinstance(clima_previsao, ClimaPrevisao)
                and isinstance(clima_previsao.id, str)):
            super().update(clima_previsao.data, clima_previsao)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
