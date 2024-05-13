from entidade.notificacao_entidade import NotificacaoEntidade


class NotificacaoControle:
    def __init__(self):
        self.__notificacoes = []

    def inclui_notificacao(self, tipo_notificacao, status):
        nova_notificacao = NotificacaoEntidade(tipo_notificacao,status)
        if nova_notificacao not in self.__notificacoes:
            self.__notificacoes.append(nova_notificacao)
    
    def remove_notificacao(self, notificacao):
        for notificacao in self.__notificacoes:
            if isinstance(notificacao, NotificacaoEntidade):
                self.__notificacoes.remove(notificacao)
    
    def altera_notificacao(self, notificacao, tipo_notificacao, status):
        for notificacao in self.__notificacoes:
            ...
        
    @property
    def listar_notificacoes(self):
        return self.__notificacoes
