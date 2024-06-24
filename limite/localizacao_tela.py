from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class LocalizacaoTela(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        self.init_opcoes()
        opcao = 0
        while True:
            button, values = self.open()
            if button is None or values is None:  # Handle window close or None events
                break
            if values['1']:
                opcao = 1
                break
            if values['2']:
                opcao = 2
                break
            if values['3']:
                opcao = 3
                break
            if values['4']:
                opcao = 4
                break
            if values['0']:
                opcao = 0
                break
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Localização', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Incluir Localização', "RD1", key='1', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Alterar Localização', "RD1", key='2', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Listar Localizações', "RD1", key='3', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Remover Localização', "RD1", key='4', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Retornar', "RD1", key='0', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Clima CO', layout, element_justification='c', finalize=True)

    def pega_dados_localizacao(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Digite os dados da localização', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text('Cidade:', font=("Helvetica", 14)), sg.InputText(key='cidade')],
            [sg.Text('Estado:', font=("Helvetica", 14)), sg.InputText(key='estado')],
            [sg.Text('País:', font=("Helvetica", 14)), sg.InputText(key='pais')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados da Localização', layout, element_justification='c', finalize=True)
        button, values = self.open()
        dados_localizacao = None
        if button == 'Confirmar':
            dados_localizacao = {"cidade": values['cidade'], "estado": values['estado'], "pais": values['pais']}
        else:
            self.close()
        self.close()
        return dados_localizacao

    def mostra_dados_localizacao(self, dados_localizacao):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Dados da Localização', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text(f"Cidade: {dados_localizacao['cidade']}", font=("Helvetica", 14))],
            [sg.Text(f"Estado: {dados_localizacao['estado']}", font=("Helvetica", 14))],
            [sg.Text(f"País: {dados_localizacao['pais']}", font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados da Localização', layout, element_justification='c', finalize=True)
        self.__window.read()
        self.close()

    def seleciona_cidade(self, lista_cidades):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Selecione a cidade', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Column([[sg.Radio(cidade, "CIDADES", key=cidade)] for cidade in lista_cidades])],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Selecionar Cidade', layout, element_justification='c', finalize=True)
        button, values = self.open()
        cidade = None
        if button == 'Confirmar':
            for key, value in values.items():
                if value:
                    cidade = key
                    break
        self.close()
        return cidade

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()
