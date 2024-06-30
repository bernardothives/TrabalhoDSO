from DAOs.dao import DAO
from entidade.notificacao import Notificacao


class NotificacaoDAO(DAO):
    def __init__(self):
        super().__init__('notificacao.pkl')

    def add(self, notificacao: Notificacao):
        if notificacao is not None and isinstance(notificacao, Notificacao) and notificacao.tipo_notificacao is not None:
            super().add(notificacao.tipo_notificacao, notificacao)

    def update(self, notificacao: Notificacao):
        if notificacao is not None and isinstance(notificacao, Notificacao) and notificacao.tipo_notificacao is not None:
            super().update(notificacao.tipo_notificacao, notificacao)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
