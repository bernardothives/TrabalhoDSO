from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from exceptions.cpf_nao_eh_numero_exception import CpfNaoEhNumero
from exceptions.cpf_tamanho_errado_exception import CpfTamanhoErrado
from exceptions.cpf_digitos_iguais_exception import CpfDigitosIguais
from exceptions.cpf_digitos_verificadores_exception import CpfDigitosVerificadores
from exceptions.nome_vazio_exception import NomeVazio
from exceptions.nome_apenas_letras_exception import NomeApenasLetras


class ClimaPrevisaoTela(TelaAbstrata):
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
            if values.get('0'):
                opcao = 0
                break
        self.close()
        return opcao

    def init_opcoes(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Previsão do Clima', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='White')],
            [sg.Text('Escolha sua opção:', font=("Helvetica", 15), pad=(10, 10), text_color='darkblue')],
            [sg.Radio('Ver Dados Climáticos', "RD1", key='1', font=("Helvetica", 14), pad=(10, 5),
                      enable_events=True, text_color='black')],
            [sg.Radio('Ver Histórico de Registro de Previsão', "RD1", key='2',
                      font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Apagar Todo o Histórico de Registro', "RD1", key='3',
                      font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Apagar Registro de Previsão Específico', "RD1", key='4',
                      font=("Helvetica", 14), pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Alertas', "RD1", key='5', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Remover Previsões de Clima', "RD1", key='6', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')],
            [sg.Radio('Retornar', "RD1", key='0', font=("Helvetica", 14),
                      pad=(10, 5), enable_events=True, text_color='black')]
        ]
        self.__window = sg.Window('Previsão do Clima', layout, element_justification='c')

    def pega_dados_ver_clima(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Dados para Ver a Previsão', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text('CPF:', font=("Helvetica", 14), size=(15, 1)), sg.InputText(key='cpf')],
            [sg.Text('Cidade:', font=("Helvetica", 14), size=(15, 1)), sg.InputText(key='cidade')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados para Ver a Previsão', layout, element_justification='left')
        button, values = self.open()
        dados_ver_clima = None
        if button == 'Confirmar':
            cpf = values['cpf']
            cidade = values['cidade']
            try:
                if not cpf or not cidade:
                    raise ValueError("CPF e Cidade não podem estar vazios.")
                cpf_valido = self.le_e_valida_cpf(cpf)
                cidade_valida = self.le_e_valida_nome(cidade)
                dados_ver_clima = {"cpf": cpf_valido, "cidade": cidade_valida}
            except (CpfDigitosIguais, CpfDigitosVerificadores, CpfNaoEhNumero,
                    CpfTamanhoErrado, NomeApenasLetras, NomeVazio, ValueError) as e:
                sg.popup(str(e), title='Erro')
        self.close()
        return dados_ver_clima

    def mostra_clima(self, dados_clima):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Dados Climáticos', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text(f"Temperatura: {dados_clima['temperatura']} graus Celsius", font=("Helvetica", 14))],
            [sg.Text(f"Humidade: {dados_clima['humidade']}%", font=("Helvetica", 14))],
            [sg.Text(f"Velocidade do Vento: {dados_clima['velocidade_vento']} km/h", font=("Helvetica", 14))],
            [sg.Text(f"Volume de Chuva: {dados_clima['volume_chuva']} mm", font=("Helvetica", 14))],
            [sg.Text(f"Visibilidade: {dados_clima['visibilidade']}%", font=("Helvetica", 14))],
            [sg.Text(f"Sensação Térmica: {dados_clima['sensacao_termica']} graus Celsius",
                     font=("Helvetica", 14))],
            [sg.Text(f"Data: {dados_clima['data']}", font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados Climáticos', layout, element_justification='center')
        self.__window.read()
        self.close()

    def seleciona_cpf(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('CPF do Usuário para Apagar Registro', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text('CPF:', font=("Helvetica", 14), size=(15, 1)), sg.InputText(key='cpf')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Apagar Registro de Previsão', layout, element_justification='left')
        button, values = self.open()
        cpf = None
        if button == 'Confirmar':
            cpf = values['cpf']
            try:
                cpf_valido = self.le_e_valida_cpf(cpf)
                return cpf_valido
            except (CpfDigitosIguais, CpfDigitosVerificadores, CpfNaoEhNumero,
                    CpfTamanhoErrado, ValueError) as e:
                sg.popup(str(e), title='Erro')
        self.close()
        return cpf

    def mostra_log(self, dados_log):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Histórico de Registro', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text(f"CPF: {dados_log['cpf']}", font=("Helvetica", 14))],
            [sg.Text(f"Cidade: {dados_log['cidade']}", font=("Helvetica", 14))],
            [sg.Text(f"Hora: {dados_log['hora']}", font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Histórico de Registro', layout, element_justification='center')
        self.__window.read()
        self.close()

    def seleciona_id(self):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Selecione o id do clima', font=("Helvetica", 25), justification='center',
                     pad=(10, 20), text_color='navy')],
            [sg.Text('id:', font=("Helvetica", 14)), sg.InputText(key='id')],
            [sg.Button('Confirmar', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5)),
             sg.Button('Cancelar', font=("Helvetica", 14), button_color=('white', 'red'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Selecionar Id', layout, element_justification='c')
        button, values = self.open()
        id_clima = None
        if button == 'Confirmar':
            id_clima = values['id']
        self.close()
        return id_clima

    def mostra_dados_clima(self, dado_clima_previsao):
        sg.theme('LightBlue3')
        layout = [
            [sg.Text('Previsões de Clima', font=("Helvetica", 25), justification='center', pad=(10, 20),
                     text_color='navy')],
            [sg.Text(f"CPF: {dado_clima_previsao['cpf']}", font=("Helvetica", 14))],
            [sg.Text(f"Cidade: {dado_clima_previsao['cidade']}", font=("Helvetica", 14))],
            [sg.Text(f"Id: {dado_clima_previsao['id']}", font=("Helvetica", 14))],
            [sg.Button('Ok', font=("Helvetica", 14), button_color=('white', 'green'), pad=(10, 5))]
        ]
        self.__window = sg.Window('Dados do Usuário', layout, element_justification='c')
        self.__window.read()
        self.close()

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()
