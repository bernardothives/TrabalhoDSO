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
        tipo = self.le_tipo()
        status = self.le_boolean()
        cpf = input("Digite o cpf do usuario notificado:")
        nome_usuario = input("Digite o nome do usuario notificado:")
        return {"tipo_notificacao": tipo, "status": status, "cpf": cpf, "nome_usuario": nome_usuario}

    @staticmethod
    def mostra_notificacao(dados_notificacao):
        print("TIPO: ", dados_notificacao["tipo_notificacao"])
        print("USUÁRIO: ", dados_notificacao["nome_usuario"])
        print("CPF: ", dados_notificacao["cpf"])
        if dados_notificacao["status"] is True:
            print("STATUS: ATIVO")
        else:
            print("STATUS: INATIVO")
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

    def pega_dados_especifico(self):
        print("-=-=-=-=- DADOS NOTIFICACAO -=-=-=-=-")
        tipo = self.le_tipo()
        status = self.le_boolean()
        cpf = input("Digite o cpf do usuario notificado:")
        return {"tipo_notificacao": tipo, "status": status, "cpf": cpf}

    @staticmethod
    def le_tipo():
        tipos_validos = ["banner", "central", "tela de bloqueio"]
        tipo_lido = input("Digite o tipo de notificacao: (ex: Banner, Central ou Tela de Bloqueio)")
        if tipo_lido.lower() not in tipos_validos:
            print("Tipo inválido, tente novamente")
            return None
        else:
            tipo = tipo_lido
            return tipo
