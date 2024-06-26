from abc import abstractmethod, ABC
import PySimpleGUI as sg


class TelaAbstrata(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass

    @staticmethod
    def le_e_valida_cpf(cpf):
        if not cpf.isdigit():
            raise ValueError("CPF deve ser composto apenas por números.")
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos.")
        if cpf == cpf[0] * len(cpf):
            raise ValueError("CPF inválido: Todos os dígitos são iguais.")
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - soma % 11
        digito1 = digito1 if digito1 < 10 else 0
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - soma % 11
        digito2 = digito2 if digito2 < 10 else 0
        if cpf[-2:] != f"{digito1}{digito2}":
            raise ValueError("CPF incorreto: Dígitos verificadores inválidos.")
        return cpf

    @staticmethod
    def le_e_valida_nome(nome):
        nome = nome.strip()
        if not nome:
            raise ValueError("Nome não pode estar vazio.")
        if not nome.replace(" ", "").isalpha():
            raise ValueError("Nome deve conter apenas letras.")
        return nome.lower()

    @staticmethod
    def mostra_msg(mensagem):
        sg.popup(mensagem, title='Mensagem')
