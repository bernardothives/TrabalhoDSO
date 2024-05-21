from limite.tela_abstrata import TelaAbstrata


class UsuarioTela(TelaAbstrata):

    def tela_opcoes(self):
        print("-=-=-=-=- USUÁRIO -=-=-=-=-")
        print("1 - Incluir usuário")
        print("2 - Alterar nome de usuario")
        print("3 - Listar Usuários")
        print("4 - Remove Usuário")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

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
