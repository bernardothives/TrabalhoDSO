from entidade.usuario import Usuario


class Notificacao:
    def __init__(self, tipo_notificacao: str, status: bool, usuario: Usuario):
        self.__tipo_notificacao = tipo_notificacao
        self.__status = status
        self.__usuario = usuario

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

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario
