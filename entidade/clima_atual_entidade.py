from entidade.clima_entidade_abstrata import ClimaEntidadeAbstrata
from datetime import datetime
from entidade.usuario_entidade import UsuarioEntidade
from entidade.localizacao_entidade import Localizacao


class ClimaAtualEntidade(ClimaEntidadeAbstrata):
    def __init__(self, usuario: UsuarioEntidade, localizacao: Localizacao):
        super().__init__(usuario, localizacao)
        self.__horario = datetime.now().strftime('%H:%M:%S')

    @property
    def horario(self):
        return self.__horario
