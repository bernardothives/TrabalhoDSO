from DAOs.dao import DAO
from entidade.notificacao import Notificacao


class NotificacaoDAO(DAO):
    def __init__(self):
        super().__init__('notificacao.pkl')

    def add(self, notificacao: Notificacao):
        if (notificacao is not None and isinstance(notificacao, Notificacao)
                and isinstance(notificacao.tipo_notificacao, str)):
            super().add(notificacao.tipo_notificacao, notificacao)

    def update(self, notificacao: Notificacao):
        if (notificacao is not None and isinstance(notificacao, Notificacao)
                and isinstance(notificacao.tipo_notificacao, str)):
            super().update(notificacao.tipo_notificacao, notificacao)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)
