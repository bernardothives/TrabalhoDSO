
class NotificacaoTela:

    @staticmethod
    def tela_opcoes():
        print("-=-=-=-=- NOTIFICACAO -=-=-=-=-")
        print("1- Ver Notificacoes.")
        print("2- Incluir Notificacao.")
        print("3- Alterar Status")
        print("4- Remover Notificacao")
        opcao = int(input("Digite a opção desejada"))
        return opcao

    @staticmethod
    def pega_dados_notificacao():
        print("-=-=-=-=- DADOS NOTIFICACAO -=-=-=-=-")
        tipo = input("Digite o tipo de notificacao:")
        status = input("Status: ")
        return {"tipo_notificacao": tipo, "status": status}

    @staticmethod
    def mostra_notificacao(dados_notificacao):
        print("TIPO: ", dados_notificacao["tipo"])
        print("STATUS: ", dados_notificacao["status"])
        print("\n")

    @staticmethod
    def seleciona_notificacao():
        tipo = input("Digite o tipo de notificacao:")
        return tipo
