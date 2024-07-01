from DAOs.dao import DAO
from entidade.clima_atual import ClimaAtual


class ClimaAtualDAO(DAO):
    def __init__(self):
        super().__init__('clima_atual.pkl')

    def add(self, clima_atual: ClimaAtual):
        if clima_atual is not None and isinstance(clima_atual, ClimaAtual) and isinstance(clima_atual.id, str):
            super().add(clima_atual.id, clima_atual)

    def update(self, clima_atual: ClimaAtual):
        if clima_atual is not None and isinstance(clima_atual, ClimaAtual) and isinstance(clima_atual.id, str):
            super().update(clima_atual.id, ClimaAtual)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
