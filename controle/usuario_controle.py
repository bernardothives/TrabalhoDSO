from entidade.usuario_entidade import UsuarioEntidade
from limite.usuario_tela import UsuarioTela


class UsuarioControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__usuarios = []
        self.__tela_usuario = UsuarioTela()

    def inclui_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        novo_usuario = UsuarioEntidade(dados_usuario["nome"], dados_usuario["cpf"])
        if self.__usuarios:
            for usuario in self.__usuarios:
                if str(usuario.cpf) == dados_usuario["cpf"]:
                    self.__tela_usuario.mostra_msg("Usuário já cadastrado \n")
            else:
                self.__usuarios.append(novo_usuario)
        else:
            self.__usuarios.append(novo_usuario)

    def alterar_nome_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario:
            novo_nome_usuario = self.__tela_usuario.pega_nome_usuario()
            for user in self.__usuarios:
                if user.nome == novo_nome_usuario["nome"]:
                    self.__tela_usuario.mostra_msg("Nome ja cadastrado \n")
                    break
            usuario.nome = novo_nome_usuario["nome"]
        else:
            self.__tela_usuario.mostra_msg("Ocorreu um erro, selecione um usuario existente. \n")

    def remove_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario is not None:
            self.__usuarios.remove(usuario)
            self.__tela_usuario.mostra_msg("Usuario excluido com sucesso!")

    def procurar_usuario_por_cpf(self, cpf):
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
                return usuario

    def listar_usuarios(self):
        if self.__usuarios:
            for usuario in self.__usuarios:
                self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "cpf": usuario.cpf})
        else:
            self.__tela_usuario.mostra_msg("A lista de usuarios está vazia :(")

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario,
                        2: self.alterar_nome_usuario,
                        3: self.listar_usuarios,
                        4: self.remove_usuario,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
