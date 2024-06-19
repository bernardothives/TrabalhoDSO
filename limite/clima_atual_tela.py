from limite.tela_abstrata import TelaAbstrata


class ClimaAtualTela(TelaAbstrata):
    def tela_opcoes(self):
        print("-=-=-=-=- CLIMA ATUAL -=-=-=-=-")
        print("Escolha a opcao")
        print("1 - Ver Dados Climáticos")
        print("2 - Ver Histórico de Registro de Climas")
        print("3 - Apagar Todo o Histórico de Registro")
        print("4 - Apagar Registro de Clima Especifico")
        print("5 - Qual Temperatura mais alta?")
        print("6 - Qual Temperatura mais baixa?")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 6, 0])
        return opcao

    @staticmethod
    def pega_dados_ver_clima():
        print("-=-=-=-=- DADOS PARA VER O CLIMA ATUAL -=-=-=-=-")
        cpf = input("Digite o CPF: ")
        cidade = input("Digite a Cidade: ")

        return {"cpf": cpf, "cidade": cidade.title()}

    @staticmethod
    def mostra_clima(dados_clima):
        print("Temperatura:", dados_clima["temperatura"], "graus celcius")
        print("Humidade:", dados_clima["humidade"], "porcento")
        print("Velocidade do Vento:", dados_clima["velocidade_vento"], "quilometros por hora")
        print("Volume de Chuva:", dados_clima["volume_chuva"], "milimetros")
        print("Visibilidade:", dados_clima["visibilidade"], "porcento")
        print("Sensacao Termica:", dados_clima["sensacao_termica"], "graus celcius")
        print("Data:", dados_clima["data"])
        print("Horario:", dados_clima["horario"])
        print("\n")

    @staticmethod
    def seleciona_cpf():
        cpf = input("CPF do usuario que deseja apagar o registro: ")
        return cpf

    @staticmethod
    def mostra_log(dados_log):
        print("CPF:", dados_log["cpf"], "CIDADE:", dados_log["cidade"], "HORA:", dados_log["hora"])
        print("\n")

    @staticmethod
    def mostra_temperatura_mais_alta(temperatura, cidade):
        print(cidade, "é a cidade mais quente, com", temperatura, "graus celcius")

    @staticmethod
    def mostra_temperatura_mais_baixa(temperatura, cidade):
        print(cidade, "é a cidade mais fria, com", temperatura, "graus celcius")
