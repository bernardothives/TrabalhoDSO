from limite.tela_abstrata import TelaAbstrata


class AlertaTela(TelaAbstrata):
    def tela_opcoes(self):
        print("-------- Alertas ----------")
        print("Escolha a opcao")
        print("1 - Alertas com Baixa Severidade")
        print("2 - Alertas com Média Severidade")
        print("3 - Alertas com Alta Severidade")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 0])
        return opcao
