from entidade.clima_abstrato import ClimaAbstrato
from datetime import datetime
from entidade.usuario import Usuario
from entidade.localizacao import Localizacao


class ClimaAtual(ClimaAbstrato):
    def __init__(self, usuario: Usuario, localizacao: Localizacao):
        super().__init__(usuario, localizacao)
        self.__horario = datetime.now().strftime('%H:%M:%S')

    @property
    def horario(self):
        return self.__horario
