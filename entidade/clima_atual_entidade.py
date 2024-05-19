from entidade.clima_entidade_abstrata import ClimaEntidadeAbstrata
from datetime import datetime


class ClimaAtualEntidade(ClimaEntidadeAbstrata):
    def __init__(self):
        self.__horario = datetime.now().strftime('%H:%M:%S')

    @property
    def horario(self):
        return self.__horario
