class NotificacaoEntidade:
    def __init__(self, tipo_notificacao: str, status: bool):
        self.__tipo_notificacao = tipo_notificacao
        self.__status = status

    @property
    def tipo_notificacao(self):
        return self.__tipo_notificacao

    @tipo_notificacao.setter
    def tipo_notificacao(self, tipo_notificacao):
        self.__tipo_notificacao = tipo_notificacao

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status
        
