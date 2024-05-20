from entidade.clima_entidade_abstrata import ClimaEntidadeAbstrata
from entidade.usuario_entidade import UsuarioEntidade
from entidade.localizacao_entidade import Localizacao
from datetime import datetime, timedelta


class ClimaPrevisaoEntidade(ClimaEntidadeAbstrata):
    def __init__(self, usuario: UsuarioEntidade, localizacao: Localizacao):
        super().__init__(usuario, localizacao)
        self.__data = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')

    @property
    def data(self):
        return self.__data
