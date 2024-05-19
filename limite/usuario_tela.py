
class UsuarioTela:

    def tela_opcoes(self):
        print("-=-=-=-=- USUÁRIO -=-=-=-=-")
        print("1- Incluir usuário.")
        print("2- Alterar nome de usuario.")
        print("3- Listar Usuários")
        print("4- Remove Usuário")
        opcao = int(input("Digite a opção desejada"))

        return opcao

    def pega_dados_usuario(self):
        print("-=-=-=-=- DADOS USUARIO -=-=-=-=-")
        nome = input("Nome de Usuário:")
        cpf = input("CPF: ")

    def mostra_usuario(self, dados_usuario):
        print("NOME DO USUÁRIO: ", dados_usuario["nome"])
        print("CPF: ", dados_usuario["cpf"])
        print("\n")

    def seleciona_usuario(self):
        cpf = input("Digite o CPF do usuario:")
        return cpf

    def mostra_mensagem(self, mensagem):
        print(mensagem)