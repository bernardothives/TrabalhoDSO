

class LocalizacaoTela:

    def tela_opcoes(self):
        print("-=-=-=-=- LOCALIZACAO -=-=-=-=-")
        print("1- Incluir Localizacao")
        print("2- Alterar Localizacao")
        print("3- Listar Localizacoes")
        print("4- Remover Localizacao")
        print("0 - Retornar")
        opcao = int(input("Digite a opcao desejada:"))
        return opcao

    def pergunta_cidade(self):
        print("-=-=-=-=-Digite sua cidade abaixo -=-=-=-=-")
        cidade = input("Cidade:")
        return cidade

    def mostra_cidades(self, dados_localizacao):
        print("Cidade: ", dados_localizacao["cidade"])
        print("\n")

    def seleciona_cidade(self):
        cidade = input("Nome da cidade que deseja selecionar:")
        return cidade



