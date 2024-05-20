from limite.tela_abstrata import TelaAbstrata


class UsuarioTela(TelaAbstrata):

    def tela_opcoes(self):
        print("-=-=-=-=- USUÁRIO -=-=-=-=-")
        print("1- Incluir usuário.")
        print("2- Alterar nome de usuario.")
        print("3- Listar Usuários")
        print("4- Remove Usuário")
        print("0- Retornar")
        opcao = self.le_inteiro("Digite a opção desejada", [1, 2, 3, 4, 0])
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
