from entidade.clima_entidade_abstrata import ClimaEntidadeAbstrata
from entidade.usuario_entidade import UsuarioEntidade
from entidade.localizacao_entidade import Localizacao


class ClimaPrevisaoEntidade(ClimaEntidadeAbstrata):
    def __init__(self, usuario: UsuarioEntidade, localizacao: Localizacao):
        super().__init__(usuario, localizacao)
        self.__descricao = ""

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
