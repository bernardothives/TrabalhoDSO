from entidade.usuario_entidade import UsuarioEntidade


class UsuarioControle:
    def __init__(self):
        self.__usuarios = []


    def inclui_usuario(self, nome, usuario_id):
        novo_usuario = UsuarioEntidade(nome, usuario_id)
        if novo_usuario not in self.__usuarios:
            self.__usuarios.append(novo_usuario)

    def remove_usuario(self, usuario: UsuarioEntidade):
        if isinstance(usuario, UsuarioEntidade):
            if usuario in self.__usuarios:
                self.__usuarios.remove(usuario)

    def procurar_usuario_id_por_nome(self, nome):
        for usuario in self.__usuarios:
            if usuario.nome == nome:
                return usuario.usuario_id

    @property
    def listar_usuarios(self):
        return self.__usuarios
    
