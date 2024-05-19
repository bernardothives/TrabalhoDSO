from abc import abstractmethod, ABC


class TelaAbstrata(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass

    @staticmethod
    def le_inteiro(mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite uma valor numerico inteiro valido")
                if inteiros_validos:
                    print("Valor validos: ", inteiros_validos)

    @staticmethod
    def mostra_msg(mensagem):
        print(mensagem)
