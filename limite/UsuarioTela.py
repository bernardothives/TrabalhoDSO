from AbstractTela import TelaAbstrata
from UsuarioControle import UsuarioControle


class UsuarioTela:

    def __init__(self):
        self.__controlador_usuario = UsuarioControle()
        self.__campo_nome_usuario = None

    def tela_opcoes(self):
        print("1- Incluir usuário.")
        print("2- Alterar nome de usuario.")
        print("3- Voltar.")
        opcao = input("Digite a opção desejada")

    def adicionar_usuario(self):
        self.__campo_nome_usuario = input("digite o nome de usuario")
        self.__controlador_usuario.inclui_usuario(self.__campo_nome_usuario, novousuario.id)
        print(f"Usuario chamado {self.__campo_nome_usuario}, cadastrado com sucesso")

    def alterar_nome_usuario(self):
        ...