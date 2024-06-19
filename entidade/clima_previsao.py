from entidade.clima_abstrato import ClimaAbstrato
from entidade.usuario import Usuario
from entidade.localizacao import Localizacao


class ClimaPrevisao(ClimaAbstrato):
    def __init__(self, usuario: Usuario, localizacao: Localizacao):
        super().__init__(usuario, localizacao)
