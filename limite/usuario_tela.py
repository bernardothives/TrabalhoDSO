from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class UsuarioTela(TelaAbstrata):
    def __init(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('LightBlue')
        layout = [
            [sg.Text('------ Usuário ------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir usuário', "RD1", key='1')],
            [sg.Radio('Alterar usuário', "RD1", key='2')],
            [sg.Radio('Listar usuários', "RD1", key='3')],
            [sg.Radio('Excluir usuário', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Clima CO.').Layout(layout)

    def pega_dados_usuario(self):
        print("-=-=-=-=- DADOS USUARIO -=-=-=-=-")
        nome = self.le_e_valida_nome("Nome de Usuário: ")
        cpf = self.le_e_valida_cpf("CPF: ")
        return {"cpf": cpf, "nome": nome}

    def pega_nome_usuario(self):
        print("-=-=-=-=- NOVO NOME -=-=-=-=-")
        nome = self.le_e_valida_nome("Nome de Usuário: ")
        return {"nome": nome}

    @staticmethod
    def mostra_usuario(dados_usuario):
        print("NOME DO USUÁRIO:", dados_usuario["nome"])
        print("CPF:", dados_usuario["cpf"])
        print("\n")

    def seleciona_usuario(self):
        cpf = self.le_e_valida_cpf("Digite o CPF do usuario: ")
        return cpf

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
