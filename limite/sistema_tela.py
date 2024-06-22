from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class SistemaTela(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [
            [sg.Text('------ CLIMA CO. ------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Usuário', "RD1", key='1')],
            [sg.Radio('Localização', "RD1", key='2')],
            [sg.Radio('Clima Atual', "RD1", key='3')],
            [sg.Radio('Previsão do Clima', "RD1", key='4')],
            [sg.Radio('Notificação', "RD1", key='5')],
            [sg.Radio('Finalizar o Sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Clima CO.').Layout(layout)

    def close(self):
        self.__window.Close()
