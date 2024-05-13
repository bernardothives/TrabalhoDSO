
class UsuarioEntidade:
    def __init__(self, nome: str, usuario_id: int):
        self.__nome = nome
        self.__usuario_id = usuario_id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def usuario_id(self):
        return self.__usuario_id
    
    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id
        
        
