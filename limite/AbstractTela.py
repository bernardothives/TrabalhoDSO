from abc import abstractmethod, ABC


class TelaAbstrata(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def tela_opcoes(self):
        ...

    @abstractmethod
    def le_inteiro(self):
        ...

    @abstractmethod
    def mostra_msg(self):
