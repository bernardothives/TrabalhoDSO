from limite.tela_abstrata import TelaAbstrata


class ClimaPrevisaoTela(TelaAbstrata):
    def tela_opcoes(self):
        print("-=-=-=-=- PREVISAO DO CLIMA -=-=-=-=-")
        print("Escolha a opcao")
        print("1 - Ver Dados Climáticos")
        print("2 - Ver Histórico de Registro de Previsao")
        print("3 - Apagar Todo o Histórico de Registro")
        print("4 - Apagar Registro de Previsao Especifico")
        print("5 - Alertas")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
        return opcao

    @staticmethod
    def pega_dados_ver_clima():
        print("-=-=-=-=- DADOS PARA VER A PREVISÃO -=-=-=-=-")
        cpf = input("Digite o CPF: ")
        cidade = input("Digite a Cidade: ")

        return {"cpf": cpf, "cidade": cidade}

    @staticmethod
    def mostra_clima(dados_clima):
        print("Temperatura:", dados_clima["temperatura"])
        print("Humidade:", dados_clima["humidade"])
        print("Velocidade do Vento:", dados_clima["velocidade_vento"])
        print("Volume de Chuva:", dados_clima["volume_chuva"])
        print("Visibilidade:", dados_clima["visibilidade"])
        print("Sensacao Termica:", dados_clima["sensacao_termica"])
        print("Data:", dados_clima["data"])
        print("\n")

    @staticmethod
    def seleciona_cpf():
        cpf = input("CPF do usuario que deseja apagar o registro: ")
        return cpf

    @staticmethod
    def mostra_log(dados_log):
        print("CPF:", dados_log["cpf"], "CIDADE:", dados_log["cidade"], "HORA:", dados_log["hora"])
        print("\n")
