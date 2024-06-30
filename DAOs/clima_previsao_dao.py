from DAOs.dao import DAO
from entidade.clima_previsao import ClimaPrevisao


class ClimaPrevisaoDAO(DAO):
    def __init__(self):
        super().__init__('clima_previsao.pkl')

    def add(self, clima_previsao: ClimaPrevisao):
        if clima_previsao is not None and isinstance(clima_previsao, ClimaPrevisao) and clima_previsao.data is not None:
            super().add(clima_previsao.data, clima_previsao)

    def update(self, clima_previsao: ClimaPrevisao):
        if clima_previsao is not None and isinstance(clima_previsao, ClimaPrevisao) and clima_previsao.data is not None:
            super().update(clima_previsao.data, ClimaPrevisao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
