
class UsuarioTela:

    @staticmethod
    def tela_opcoes():
        print("-=-=-=-=- USUÁRIO -=-=-=-=-")
        print("1- Incluir usuário.")
        print("2- Alterar nome de usuario.")
        print("3- Listar Usuários")
        print("4- Remove Usuário")
        opcao = int(input("Digite a opção desejada"))
        return opcao

    @staticmethod
    def pega_dados_usuario():
        print("-=-=-=-=- DADOS USUARIO -=-=-=-=-")
        nome = input("Nome de Usuário:")
        cpf = input("CPF: ")
        return {"cpf": cpf, "nome": nome}

    @staticmethod
    def mostra_usuario(dados_usuario):
        print("NOME DO USUÁRIO: ", dados_usuario["nome"])
        print("CPF: ", dados_usuario["cpf"])
        print("\n")

    @staticmethod
    def seleciona_usuario():
        cpf = input("Digite o CPF do usuario:")
        return cpf
