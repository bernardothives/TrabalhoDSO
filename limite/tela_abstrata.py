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
    def le_e_valida_nome(mensagem: str = ""):
        while True:
            nome = input(mensagem).strip()
            if not nome:
                print("Nome incorreto: O nome não pode estar vazio. Tente novamente.")
                continue

            if " " in nome or not nome.isalpha():
                print("Nome incorreto: O nome deve ser uma única palavra contendo apenas letras. Tente novamente.")
                continue

            return nome.lower()

    @staticmethod
    def le_e_valida_cpf(mensagem: str = ""):
        while True:
            cpf = input(mensagem).strip()
            if not cpf.isdigit():
                print("CPF incorreto: Deve ser composto apenas por números. Tente novamente.")
                continue

            if len(cpf) != 11:
                print("CPF incorreto: Deve conter 11 dígitos. Tente novamente.")
                continue

            if cpf == cpf[0] * len(cpf):
                print("CPF incorreto: Todos os dígitos são iguais. Tente novamente.")
                continue

            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            digito1 = 11 - soma % 11
            digito1 = digito1 if digito1 < 10 else 0

            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            digito2 = 11 - soma % 11
            digito2 = digito2 if digito2 < 10 else 0

            if cpf[-2:] == f"{digito1}{digito2}":
                return cpf
            else:
                print("CPF incorreto: Dígitos verificadores inválidos. Tente novamente.")

    @staticmethod
    def mostra_msg(mensagem):
        print(mensagem)
