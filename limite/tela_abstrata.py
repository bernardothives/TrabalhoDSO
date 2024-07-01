from abc import abstractmethod, ABC
import PySimpleGUI as sg
from exceptions.cpf_nao_eh_numero_exception import CpfNaoEhNumero
from exceptions.cpf_tamanho_errado_exception import CpfTamanhoErrado
from exceptions.cpf_digitos_iguais_exception import CpfDigitosIguais
from exceptions.cpf_digitos_verificadores_exception import CpfDigitosVerificadores
from exceptions.nome_vazio_exception import NomeVazio
from exceptions.nome_apenas_letras_exception import NomeApenasLetras

class TelaAbstrata(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass

    def le_e_valida_cpf(self, cpf):
        if not cpf.isdigit():
            raise CpfNaoEhNumero()
        if len(cpf) != 11:
            raise CpfTamanhoErrado()
        if cpf == cpf[0] * len(cpf):
            raise CpfDigitosIguais()
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - soma % 11
        digito1 = digito1 if digito1 < 10 else 0
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - soma % 11
        digito2 = digito2 if digito2 < 10 else 0
        if cpf[-2:] != f"{digito1}{digito2}":
            raise CpfDigitosVerificadores()
        return cpf

    def le_e_valida_nome(self, nome):
        nome = nome.strip()
        if not nome:
            raise NomeVazio()
        if not nome.replace(" ", "").isalpha():
            raise NomeApenasLetras()
        return nome.lower()

    def mostra_msg(self, mensagem):
        sg.popup(mensagem, title='Mensagem')
