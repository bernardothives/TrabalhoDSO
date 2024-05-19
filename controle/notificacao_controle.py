from entidade.notificacao_entidade import NotificacaoEntidade
from limite.notificacao_tela import NotificacaoTela

class NotificacaoControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__tela_notificacao = NotificacaoTela()
        self.__notificacoes = []

    def inclui_notificacao(self, tipo_notificacao, status):
        dados_notificacao = self.__tela_notificacao.pega_dados_notificacao()
        notificacao = NotificacaoEntidade(dados_notificacao["tipo_notificacao"], dados_notificacao["status"])
        self.__notificacoes.append(notificacao)

    def remove_notificacao(self, notificacao):
        self.listar_notificacoes()
        tipo = self.__tela_notificacao.seleciona_notificacao()
        notificacao = self.procura_notificacao_por_tipo(tipo)
        if notificacao is not None:
            self.__notificacoes.remove(notificacao)
            self.listar_notificacoes()
    
    def altera_notificacao(self, notificacao, tipo_notificacao, status):
        self.listar_notificacoes()
        tipo_notificacao = self.__tela_notificacao.seleciona_notificacao()
        notificacao = self.procura_notificacao_por_tipo(tipo_notificacao)
        if notificacao is not None:
            novos_dados_notificacao = self.__tela_notificacao.pega_dados_notificacao()
            notificacao.tipo_notificacao = novos_dados_notificacao["tipo"]
            notificacao.status = novos_dados_notificacao["status"]

    def procura_notificacao_por_tipo(self, tipo):
        for notificacao in self.__notificacoes:
            if notificacao.tipo_notificacao == tipo:
                return notificacao

    def listar_notificacoes(self):
        for notifficacao in self.__notificacoes:
            self.__tela_notificacao.mostra_notificacao({"tipo": notifficacao.tipo_notificacao,
                                                        "status": notifficacao.status})
    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.listar_notificacoes,
                        2: self.inclui_notificacao,
                        3: self.altera_notificacao,
                        4: self.remove_notificacao,
                        0: self.retornar}
