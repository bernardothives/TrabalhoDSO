from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class NotificacaoTela(TelaAbstrata):
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
            [sg.Text('Notificação', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Ver Notificações', "RD1", key='1', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Incluir Notificação', "RD1", key='2', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Alterar Status', "RD1", key='3', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Remover Notificação', "RD1", key='4', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Retornar', "RD1", key='0', font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Notificações', layout, element_justification='c', finalize=True)

    def pega_dados_notificacao(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Dados da Notificação', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text('Tipo de Notificação:', font=("Helvetica", 14)), sg.InputText(key='tipo_notificacao')],
            [sg.Text('Status (Sim/Nao):', font=("Helvetica", 14)), sg.InputText(key='status')],
            [sg.Text('CPF do Usuário Notificado:', font=("Helvetica", 14)), sg.InputText(key='cpf')],
            [sg.Text('Nome do Usuário Notificado:', font=("Helvetica", 14)), sg.InputText(key='nome_usuario')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados da Notificação', layout, element_justification='c', finalize=True)
        button, values = self.open()
        dados_notificacao = None
        if button == 'Confirmar':
            tipo = values['tipo_notificacao']
            status = True if values['status'].lower() == 'sim' else False
            dados_notificacao = {
                "tipo_notificacao": tipo,
                "status": status,
                "cpf": values['cpf'],
                "nome_usuario": values['nome_usuario']
            }
        else:
            self.close()
        self.close()
        return dados_notificacao

    def mostra_notificacao(self, dados_notificacao):
        sg.theme('LightBlue3')
        status_text = 'ATIVO' if dados_notificacao["status"] else 'INATIVO'
        layout = [
            [sg.Text('Dados da Notificação', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text(f"TIPO: {dados_notificacao['tipo_notificacao']}", font=("Helvetica", 14))],
            [sg.Text(f"USUÁRIO: {dados_notificacao['nome_usuario']}", font=("Helvetica", 14))],
            [sg.Text(f"CPF: {dados_notificacao['cpf']}", font=("Helvetica", 14))],
            [sg.Text(f"STATUS: {status_text}", font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados da Notificação', layout, element_justification='c', finalize=True)
        self.__window.read()
        self.close()

    def seleciona_notificacao(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Selecione Notificação', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text('Tipo de Notificação:', font=("Helvetica", 14)), sg.InputText(key='tipo_notificacao')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Selecionar Notificação', layout, element_justification='c', finalize=True)
        button, values = self.open()
        tipo = None
        if button == 'Confirmar':
            tipo = values['tipo_notificacao']
        else:
            self.close()
        self.close()
        return tipo

    def pega_dados_especifico(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Dados da Notificação Específica', font=("Helvetica", 25), justification='center', pad=(10, 20), text_color='navy')],
            [sg.Text('Tipo de Notificação:', font=("Helvetica", 14)), sg.InputText(key='tipo_notificacao')],
            [sg.Text('Status (Sim/Nao):', font=("Helvetica", 14)), sg.InputText(key='status')],
            [sg.Text('CPF do Usuário Notificado:', font=("Helvetica", 14)), sg.InputText(key='cpf')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Cancel('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados da Notificação Específica', layout, element_justification='c', finalize=True)
        button, values = self.open()
        dados_notificacao = None
        if button == 'Confirmar':
            tipo = values['tipo_notificacao']
            status = True if values['status'].lower() == 'sim' else False
            dados_notificacao = {
                "tipo_notificacao": tipo,
                "status": status,
                "cpf": values['cpf']
            }
        else:
            self.close()
        self.close()
        return dados_notificacao

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()
