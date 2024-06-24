from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class AlertaTela(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        self.init_opcoes()
        opcao = 0
        while True:
            button, values = self.open()
            if button is None or values is None:
                break
            if values['1']:
                opcao = 1
                break
            if values['0']:
                opcao = 0
                break
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Alertas', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Ver Alerta', "RD1", key='1', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Retornar', "RD1", key='0', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Alertas', layout, element_justification='c', finalize=True)

    def seleciona_cidade(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Verificar Alerta', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text('Cidade:', font=("Helvetica", 14)), sg.InputText(key='cidade')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Verificar Alerta', layout, element_justification='c', finalize=True)
        button, values = self.open()
        cidade = None
        if button == 'Confirmar':
            cidade = values['cidade']
        self.close()
        return cidade

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()
