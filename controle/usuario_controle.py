from entidade.usuario import Usuario
from limite.usuario_tela import UsuarioTela
from DAOs.usuario_dao import UsuarioDAO
from exceptions.usuario_duplicado_exception import UsuarioDuplicado


class UsuarioControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__usuario_DAO = UsuarioDAO()
        self.__tela_usuario = UsuarioTela()

    def inclui_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        if dados_usuario:
            usuario = self.procurar_usuario_por_cpf(dados_usuario['cpf'])
            if usuario:
                raise UsuarioDuplicado()
            else:
                usuario = Usuario(dados_usuario["nome"], dados_usuario["cpf"])
                self.__usuario_DAO.add(usuario)

    def alterar_nome_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario:
            novo_nome_usuario = self.__tela_usuario.pega_nome_usuario()
            for user in self.__usuario_DAO.get_all():
                if user.nome == novo_nome_usuario["nome"]:
                    self.__tela_usuario.mostra_msg("Nome ja cadastrado \n")
                    break
            usuario.nome = novo_nome_usuario["nome"]
        #else:
        #    self.__tela_usuario.mostra_msg("Ocorreu um erro, selecione um usuario existente. \n")

    def remove_usuario(self):
        self.listar_usuarios()
        cpf_usuario = self.__tela_usuario.seleciona_usuario()
        usuario = self.procurar_usuario_por_cpf(cpf_usuario)
        if usuario is not None:
            self.__usuarios.remove(usuario)
            self.__tela_usuario.mostra_msg("Usuario excluido com sucesso!")

    def procurar_usuario_por_cpf(self, cpf):
        return self.__usuario_DAO.get(cpf)

    def listar_usuarios(self):
        self.__tela_usuario.mostra_msg("--- Lista de Usuários: ---")
        usuarios = self.__usuario_DAO.get_all()
        for usuario in usuarios:
            dados_usuario = {usuario.nome: usuario.cpf}
            self.__tela_usuario.mostra_usuario(dados_usuario)


    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_usuario,
            2: self.alterar_nome_usuario,
            3: self.listar_usuarios,
            4: self.remove_usuario,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_usuario.tela_opcoes()
            if opcao == 0:
                break
            lista_opcoes[opcao]()
