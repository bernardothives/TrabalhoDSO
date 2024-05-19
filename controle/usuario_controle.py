from entidade.usuario_entidade import UsuarioEntidade
from limite.usuario_tela import UsuarioTela


class UsuarioControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__usuarios = []
        self.__tela_usuario = UsuarioTela()

    def inclui_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        usuario = UsuarioEntidade(dados_usuario["nome"], dados_usuario["cpf"])
        self.__usuarios.append(usuario)

    def alterar_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario is not None:
            novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
            usuario.nome = novos_dados_usuario["nome"]
            usuario.cpf = novos_dados_usuario["cpf"]

    def remove_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario is not None:
            self.__usuarios.remove(usuario)
            self.listar_usuarios()

    def procurar_usuario_por_cpf(self, cpf):
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
                return usuario

    def listar_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "cpf": usuario.cpf})

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario,
                        2: self.alterar_usuario,
                        3: self.listar_usuarios,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()


