from limite.tela_abstrata import TelaAbstrata


class LocalizacaoTela(TelaAbstrata):

    def tela_opcoes(self):
        print("-=-=-=-=- LOCALIZACAO -=-=-=-=-")
        print("1 - Incluir Localizacao")
        print("2 - Alterar Localizacao")
        print("3 - Listar Localizacoes")
        print("4 - Remover Localizacao")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    @staticmethod
    def pega_dados_localizacaoe():
        print("-=-=-=-=-DADOS LOCALIZACAO -=-=-=-=-")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        pais = input("País: ")
        return {"cidade": cidade, "estado": estado, "pais": pais}

    @staticmethod
    def mostra_dados_localizacao( dados_localizacao):
        print("Cidade: ", dados_localizacao["cidade"])
        print("Estado: ", dados_localizacao["estado"])
        print("País: ", dados_localizacao["pais"])
        print("\n")

    @staticmethod
    def seleciona_cidade():
        cidade = input("Nome da cidade que deseja selecionar: ")
        return cidade
