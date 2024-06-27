from DAOs.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and usuario.cpf is not None:
            super().add(usuario.cpf, usuario)

    def update(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and usuario.cpf is not None:
            super().update(usuario.cpf, usuario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
