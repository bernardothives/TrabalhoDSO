from limite.tela_abstrata import TelaAbstrata


class SistemaTela(TelaAbstrata):
    def tela_opcoes(self):
        print("-=-=-=-=- CLIMACO -=-=-=-=-")
        print("Escolha sua opcao")
        print("1 - Usuário")
        print("2 - Localização")
        print("3 - Clima Atual")
        print("4 - Previsão do Clima")
        print("5 - Notificação")
        print("0 - Finalizar sistema")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
        return opcao
