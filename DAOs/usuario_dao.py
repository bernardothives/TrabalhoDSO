from DAOs.dao import DAO
from entidade.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(usuario.cpf, str):
            super().add(usuario.cpf, usuario)

    def update(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(usuario.cpf, str):
            super().update(usuario.cpf, usuario)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
