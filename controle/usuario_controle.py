from entidade.usuario_entidade import UsuarioEntidade
from limite.usuario_tela import UsuarioTela


class UsuarioControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__usuarios = []
        self.__tela_usuario = UsuarioTela()

    def inclui_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        if self.validar_cpf(dados_usuario["cpf"]):
            novo_usuario = UsuarioEntidade(dados_usuario["nome"], dados_usuario["cpf"])
            if self.__usuarios:
                for usuario in self.__usuarios:
                    if str(usuario.cpf) == dados_usuario["cpf"]:
                        self.__tela_usuario.mostra_msg("Usuário já cadastrado, tente novamente")
                        break
                else:
                    self.__usuarios.append(novo_usuario)
            else:
                self.__usuarios.append(novo_usuario)
        else:
            self.__tela_usuario.mostra_msg("Cpf inválido, tente novamente")

    def alterar_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario is not None:
            novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
            if self.validar_cpf(novos_dados_usuario["cpf"]):
                for usuario in self.__usuarios:
                    if usuario.cpf == novos_dados_usuario["cpf"]:
                        self.__tela_usuario.mostra_msg("Cpf já cadastrado, tente novamente")
                        break
                usuario.nome = novos_dados_usuario["nome"]
                usuario.cpf = novos_dados_usuario["cpf"]
            else:
                self.__tela_usuario.mostra_msg("Cpf inválido, tente novamente")
        else:
            self.__tela_usuario.mostra_msg("Ocorreu um erro ao inserir um usuario, tente novamente")

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
        if self.__usuarios:
            for usuario in self.__usuarios:
                self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "cpf": usuario.cpf})
        else:
            self.__tela_usuario.mostra_msg("A lista de usuarios está vazia :(")

    @staticmethod
    def validar_cpf(cpf_usuario):
        cpf_usuario = str(cpf_usuario)

        if len(cpf_usuario) != 11:
            return False

        if cpf_usuario == cpf_usuario[0] * 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf_usuario[i]) * (10 - i)
        dv1 = 11 - (soma % 11)
        if dv1 >= 10:
            dv1 = 0

        soma = 0
        for i in range(10):
            soma += int(cpf_usuario[i]) * (11 - i)
        dv2 = 11 - (soma % 11)
        if dv2 >= 10:
            dv2 = 0

        return cpf_usuario[-2:] == f'{dv1}{dv2}'

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario,
                        2: self.alterar_usuario,
                        3: self.listar_usuarios,
                        4: self.remove_usuario,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
