from limite.tela_abstrata import TelaAbstrata


class AlertaTela(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Alertas ----------")
        print("Escolha a opcao")
        print("1 - Ver Alerta")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 0])
        return opcao

    @staticmethod
    def seleciona_cidade():
        cidade = input("Cidade que deseja verificar o alerta: ")
        return cidade
