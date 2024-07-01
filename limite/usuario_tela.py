from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from exceptions.cpf_nao_eh_numero_exception import CpfNaoEhNumero
from exceptions.cpf_tamanho_errado_exception import CpfTamanhoErrado
from exceptions.cpf_digitos_iguais_exception import CpfDigitosIguais
from exceptions.cpf_digitos_verificadores_exception import CpfDigitosVerificadores
from exceptions.nome_vazio_exception import NomeVazio
from exceptions.nome_apenas_letras_exception import NomeApenasLetras


class UsuarioTela(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        self.init_opcoes()
        opcao = 0
        while True:
            button, values = self.open()
            if button is None or values is None:
                break
            if values.get('1'):
                opcao = 1
                break
            if values.get('2'):
                opcao = 2
                break
            if values.get('3'):
                opcao = 3
                break
            if values.get('4'):
                opcao = 4
                break
            if values.get('0'):
                opcao = 0
                break
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Usuário', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Incluir usuário', "RD1", key='1', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Alterar usuário', "RD1", key='2', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Listar usuários', "RD1", key='3', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Excluir usuário', "RD1", key='4', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Retornar', "RD1", key='0', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Clima CO', layout, element_justification='c', finalize=True)

    def pega_dados_usuario(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Digite os dados do usuário', font=("Helvetica", 25), justification='center', pad=(10, 20),
                     text_color='navy')],
            [sg.Text('Nome:', font=("Helvetica", 14), size=(10, 1)), sg.InputText(key='nome')],
            [sg.Text('CPF:', font=("Helvetica", 14), size=(10, 1)), sg.InputText(key='cpf')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados do Usuário', layout, element_justification='c', finalize=True)
        button, values = self.open()
        dados_usuario = None
        if button == 'Confirmar':
            cpf = values['cpf']
            nome = values['nome']
            try:
                if not cpf or not nome:
                    raise ValueError("Nome e CPF não podem estar vazios.")
                cpf_valido = self.le_e_valida_cpf(cpf)
                nome_valido = self.le_e_valida_nome(nome)
                dados_usuario = {"nome": nome_valido, "cpf": cpf_valido}
            except (CpfDigitosIguais, CpfDigitosVerificadores, CpfNaoEhNumero,
                    CpfTamanhoErrado, NomeApenasLetras, NomeVazio, ValueError) as e:
                sg.popup(str(e), title='Erro')
        else:
            self.close()
        self.close()
        return dados_usuario

    def pega_nome_usuario(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Digite o novo nome do usuário', font=("Helvetica", 25), justification='center', pad=(10, 20),
                     text_color='navy')],
            [sg.Text('Nome:', font=("Helvetica", 14)), sg.InputText(key='nome')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Novo Nome', layout, element_justification='c', finalize=True)
        button, values = self.open()
        nome = None
        if button == 'Confirmar':
            nome = values['nome']
            try:
                if not nome:
                    raise ValueError("O nome não pode estar vazio.")
                nome_valido = self.le_e_valida_nome(nome)
                self.close()
                return {"nome": nome_valido}
            except (NomeApenasLetras, NomeVazio, ValueError) as e:
                sg.popup(str(e), title='Erro')
        self.close()
        return nome

    def mostra_usuario(self, dados_usuario):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Dados do Usuário', font=("Helvetica", 25), justification='center', pad=(10, 20),
                     text_color='navy')],
            [sg.Text(f"Nome: {dados_usuario['nome']}", font=("Helvetica", 14))],
            [sg.Text(f"CPF: {dados_usuario['cpf']}", font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados do Usuário', layout, element_justification='c', finalize=True)
        self.__window.read()
        self.close()

    def seleciona_usuario(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Selecione o usuário pelo CPF', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text('CPF:', font=("Helvetica", 14)), sg.InputText(key='cpf')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Selecionar Usuário', layout, element_justification='c', finalize=True)
        button, values = self.open()
        cpf = None
        if button == 'Confirmar':
            cpf = values['cpf']
            try:
                if not cpf:
                    raise ValueError("O CPF não pode estar vazio.")
                cpf = self.le_e_valida_cpf(cpf)
            except (CpfDigitosIguais, CpfDigitosVerificadores, CpfNaoEhNumero,
                    CpfTamanhoErrado, ValueError) as e:
                sg.popup(str(e), title='Erro')
                cpf = None
        else:
            self.close()
        self.close()
        return cpf

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()
