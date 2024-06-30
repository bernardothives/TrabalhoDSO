from DAOs.dao import DAO
from entidade.clima_atual import ClimaAtual


class ClimaAtualDAO(DAO):
    def __init__(self):
        super().__init__('clima_atual.pkl')

    def add(self, clima_atual: ClimaAtual):
        if clima_atual is not None and isinstance(clima_atual, ClimaAtual) and clima_atual.horario is not None:
            super().add(clima_atual.horario, clima_atual)

    def update(self, clima_atual: ClimaAtual):
        if clima_atual is not None and isinstance(clima_atual, ClimaAtual) and clima_atual.horario is not None:
            super().update(clima_atual.horario, ClimaAtual)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
