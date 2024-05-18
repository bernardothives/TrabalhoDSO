class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisLivros ---------")
        print("Escolha sua opcao")
        print("1 - Usuário")
        print("2 - Localização")
        print("3 - Clima Atual")
        print("4 - Previsão do Clima")
        print("5 - Notificação")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao