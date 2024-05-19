from limite.sistema_tela import SistemaTela
from controle.clima_atual_controle import ClimaAtualControle
from controle.clima_previsao_controle import ClimaPrevisaoControle
from controle.localizacao_controle import LocalizacaoControle
from controle.usuario_controle import UsuarioControle
from controle.notificacao_controle import NotificacaoControle


class Sistema:
    def __init__(self):
        self.__controlador_clima_atual = ClimaAtualControle()
        self.__controlador_clima_previsao = ClimaPrevisaoControle()
        self.__controlador_localizacao = LocalizacaoControle()
        self.__controlador_usuario = UsuarioControle()
        self.__controlador_notificacao = NotificacaoControle()
        self.__sistema_tela = SistemaTela()

    def inicializa_sistema(self):
        self.abre_tela()

    def opcoes_usuario(self):
        self.__controlador_usuario.abre_tela()

    def opcoes_localizacao(self):
        self.__controlador_localizacao.abre_tela()

    def opcoes_clima_atual(self):
        self.__controlador_clima_atual.abre_tela()

    def opcoes_clima_previsao(self):
        self.__controlador_clima_previsao.abre_tela()

    def opcoes_notificacao(self):
        self.__controlador_notificacao.abre_tela()

    @staticmethod
    def encerra_sistema():
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.opcoes_usuario, 2: self.opcoes_localizacao, 3: self.opcoes_clima_atual,
                        4: self.opcoes_clima_previsao, 5: self.opcoes_notificacao, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__sistema_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
