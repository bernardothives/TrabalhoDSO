from DAOs.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(usuario.cpf, int):
            super().add(usuario.cpf, usuario)

    def update(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(usuario.cpf, int):
            super().update(usuario.cpf, usuario)

    def get(self, cpf: int):
        if isinstance(cpf, int):
            return super().get(cpf)

    def remove(self, cpf: int):
        if isinstance(cpf, int):
            return super().remove(cpf)
