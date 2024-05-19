
class NotificacaoTela:

    def tela_opcoes(self):
        print("-=-=-=-=- NOTIFICACAO -=-=-=-=-")
        print("1- Ver Notificacoes.")
        print("2- Incluir Notificacao.")
        print("3- Alterar Status")
        print("4- Remover Notificacao")
        opcao = int(input("Digite a opção desejada"))

        return opcao

    def pega_dados_notificacao(self):
        print("-=-=-=-=- DADOS NOTIFICACAO -=-=-=-=-")
        tipo = input("Digite o tipo de notificacao:")
        status = input("Status: ")

    def mostra_notificacao(self, dados_notificacao):
        print("TIPO: ", dados_notificacao["tipo"])
        print("STATUS: ", dados_notificacao["status"])
        print("\n")

    def seleciona_notificacao(self):
        tipo = input("Digite o tipo de notificacao:")
        return tipo
