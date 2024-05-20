from limite.tela_abstrata import TelaAbstrata


class NotificacaoTela(TelaAbstrata):

    def tela_opcoes(self):
        print("-=-=-=-=- NOTIFICACAO -=-=-=-=-")
        print("1 - Ver Notificacoes")
        print("2 - Incluir Notificacao")
        print("3 - Alterar Status")
        print("4 - Remover Notificacao")
        print("0 - Retornar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_notificacao(self):
        print("-=-=-=-=- DADOS NOTIFICACAO -=-=-=-=-")
        tipo = input("Digite o tipo de notificacao: ")
        status = self.le_boolean()
        return {"tipo_notificacao": tipo, "status": status}

    @staticmethod
    def mostra_notificacao(dados_notificacao):
        print("TIPO: ", dados_notificacao["tipo"])
        print("STATUS: ", dados_notificacao["status"])
        print("\n")

    @staticmethod
    def seleciona_notificacao():
        tipo = input("Digite o tipo de notificacao: ")
        return tipo

    @staticmethod
    def le_boolean():
        status_lido = input("Digite se a notificacao esta ativa('Sim' ou 'Nao'):")
        if status_lido.lower() == "sim":
            return True
        if status_lido.lower() == "nao":
            return False
        print("Valores validos: 'Sim' e 'Nao'")
