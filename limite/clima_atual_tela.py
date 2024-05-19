from limite.tela_abstrata import TelaAbstrata


class ClimaAtualTela(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Clima Atual ----------")
        print("Escolha a opcao")
        print("1 - Ver Dados Climáticos")
        print("2 - Ver Histórico de Registro de Climas")
        print("3 - Apagar Todo o Histórico de Registro")
        print("4 - Apagar Registro de Clima Especifico")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    @staticmethod
    def pega_dados_ver_clima():
        print("-------- DADOS PARA VER O CLIMA ----------")
        cpf = input("Seu CPF: ")
        localizacao = input("Localização: ")

        return {"cpf": cpf, "codigo": localizacao}
