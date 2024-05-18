from limite.sistema_tela import SistemaTela
from controle.clima_atual_controle import ClimaAtualControle
#from controle.clima_previsao_controle import ClimaPrevisaoControle
from controle.localizacao_controle import LocalizacaoControle
from controle.usuario_controle import UsuarioControle
from controle.notificacao_controle import NotificacaoControle
class Sistema:
    def __init__(self):
        self.__controlador_clima_atual = ClimaAtualControle()
        #self.__controlador_previsao_atual = ClimaPrevisaoControle()
        self.__controlador_localizacao = LocalizacaoControle()
        self.__controlador_usuario = UsuarioControle()
        self.__controlador_notificacao = NotificacaoControle()
