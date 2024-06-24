from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class SistemaTela(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        opcao = 0
        while True:
            event, values = self.__window.read()
            if event is None or values is None:
                opcao = 0
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
            if values['5']:
                opcao = 5
                break
            if values['0']:
                opcao = 0
                break
        self.close()
        return opcao

    def init_components(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Image('limite/nuvem.png'), sg.Text('Clima CO', font=("Helvetica", 30), justification='center', pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 16), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Usuário', "RD1", key='1', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Localização', "RD1", key='2', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Clima Atual', "RD1", key='3', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Previsão do Clima', "RD1", key='4', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Notificação', "RD1", key='5', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Finalizar o Sistema', "RD1", key='0', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Clima CO', layout, element_justification='c')

    def close(self):
        self.__window.close()
