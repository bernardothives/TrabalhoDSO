import PySimpleGUI as sg
from limite.tela_abstrata import TelaAbstrata
from exceptions.cpf_nao_eh_numero_exception import CpfNaoEhNumero
from exceptions.cpf_tamanho_errado_exception import CpfTamanhoErrado
from exceptions.cpf_digitos_iguais_exception import CpfDigitosIguais
from exceptions.cpf_digitos_verificadores_exception import CpfDigitosVerificadores
from exceptions.nome_vazio_exception import NomeVazio
from exceptions.nome_apenas_letras_exception import NomeApenasLetras


class ClimaAtualTela(TelaAbstrata):
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
            if values.get('5'):
                opcao = 5
                break
            if values.get('6'):
                opcao = 6
                break
            if values.get('7'):
                opcao = 7
                break
            if values.get('0'):
                opcao = 0
                break
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Clima Atual', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Ver Dados Climáticos', "RD1", key='1', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Ver Histórico de Registro de Climas', "RD1", key='2', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Apagar Todo o Histórico de Registro', "RD1", key='3', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Apagar Registro de Clima Específico', "RD1", key='4', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Qual Temperatura mais alta?', "RD1", key='5', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Qual Temperatura mais baixa?', "RD1", key='6', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Remover dados climáticos', "RD1", key='7', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Retornar', "RD1", key='0', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Clima Atual', layout, element_justification='c')

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()

    def pega_dados_ver_clima(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Digite os dados para ver o clima atual', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text('CPF:', font=("Helvetica", 14), size=(10, 1)), sg.InputText(key='cpf')],
            [sg.Text('Cidade:', font=("Helvetica", 14), size=(10, 1)), sg.InputText(key='cidade')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados para Ver o Clima Atual', layout, element_justification='c')
        button, values = self.open()
        dados_clima = None
        if button == 'Confirmar':
            cpf = values['cpf']
            cidade = values['cidade']
            try:
                if not cpf or not cidade:
                    raise ValueError("CPF e Cidade não podem estar vazios.")
                cpf_valido = self.le_e_valida_cpf(cpf)
                cidade_valida = self.le_e_valida_nome(cidade)
                dados_clima = {"cpf": cpf_valido, "cidade": cidade_valida}
            except (CpfDigitosIguais, CpfDigitosVerificadores, CpfNaoEhNumero,
                    CpfTamanhoErrado, NomeApenasLetras, NomeVazio, ValueError) as e:
                sg.popup(str(e), title='Erro')
        self.close()
        return dados_clima

    def mostra_clima(self, dados_clima):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Temperatura: {} graus Celsius'.format(dados_clima['temperatura']), font=("Helvetica", 14))],
            [sg.Text('Humidade: {}%'.format(dados_clima['humidade']), font=("Helvetica", 14))],
            [sg.Text('Velocidade do Vento: {} km/h'.format(dados_clima['velocidade_vento']), font=("Helvetica", 14))],
            [sg.Text('Volume de Chuva: {} mm'.format(dados_clima['volume_chuva']), font=("Helvetica", 14))],
            [sg.Text('Visibilidade: {}%'.format(dados_clima['visibilidade']), font=("Helvetica", 14))],
            [sg.Text('Sensação Térmica: {} graus Celsius'.format(dados_clima['sensacao_termica']),
                     font=("Helvetica", 14))],
            [sg.Text('Data: {}'.format(dados_clima['data']), font=("Helvetica", 14))],
            [sg.Text('Horário: {}'.format(dados_clima['horario']), font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados do Clima', layout, element_justification='c')
        self.__window.read()
        self.close()

    def seleciona_cpf(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Digite o CPF:', font=("Helvetica", 14)), sg.InputText(key='cpf')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Selecionar CPF', layout, element_justification='c')
        button, values = self.open()
        cpf = None
        if button == 'Confirmar':
            cpf = values['cpf']
            try:
                if not cpf:
                    raise ValueError("O CPF não pode estar vazio.")
                cpf_valido = self.le_e_valida_cpf(cpf)
                self.close()
                return cpf_valido
            except (CpfDigitosIguais, CpfDigitosVerificadores, CpfNaoEhNumero,
                    CpfTamanhoErrado, ValueError) as e:
                sg.popup(str(e), title='Erro')
                cpf = None
        self.close()
        return cpf

    def mostra_log(self, dados_log):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('CPF: {}'.format(dados_log["cpf"]), font=("Helvetica", 14))],
            [sg.Text('Cidade: {}'.format(dados_log["cidade"]), font=("Helvetica", 14))],
            [sg.Text('Hora: {}'.format(dados_log["hora"]), font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Registro de Clima', layout, element_justification='c')
        self.__window.read()
        self.close()

    def mostra_temperatura_mais_alta(self, temperatura, cidade):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('{} é a cidade mais quente, com {} graus Celsius'.format(cidade, temperatura),
                     font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Temperatura Mais Alta', layout, element_justification='c')
        self.__window.read()
        self.close()

    def seleciona_cidade(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Selecione a cidade', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text('Cidade:', font=("Helvetica", 14)), sg.InputText(key='cidade')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Selecionar Cidade', layout, element_justification='c')
        button, values = self.open()
        cidade = None
        if button == 'Confirmar':
            cidade = values['cidade']
        self.close()
        return cidade

    def mostra_temperatura_mais_baixa(self, temperatura, cidade):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('{} é a cidade mais fria, com {} graus Celsius'.format(cidade, temperatura),
                     font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Temperatura Mais Baixa', layout, element_justification='c')
        self.__window.read()
        self.close()
