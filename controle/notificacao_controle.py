from entidade.notificacao import Notificacao
from limite.notificacao_tela import NotificacaoTela


class NotificacaoControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__tela_notificacao = NotificacaoTela()
        self.__notificacoes = []

    def inclui_notificacao(self):
        dados_notificacao = self.__tela_notificacao.pega_dados_especifico()
        if dados_notificacao:
            if dados_notificacao["status"] and dados_notificacao["tipo_notificacao"]:
                nova_notificacao = Notificacao(dados_notificacao["tipo_notificacao"],
                                                dados_notificacao["status"],
                                                self.__sistema.controlador_usuario.procurar_usuario_por_cpf(
                                                            dados_notificacao["cpf"]))
                if self.__notificacoes:
                    for notificacao in self.__notificacoes:
                        if notificacao.tipo_notificacao == dados_notificacao["tipo_notificacao"]:
                            self.__tela_notificacao.mostra_msg("Tipo de notificacao já cadastrado, adicione outro tipo")
                            break
                    else:
                        self.__notificacoes.append(nova_notificacao)
                else:
                    self.__notificacoes.append(nova_notificacao)
            else:
                self.__tela_notificacao.mostra_msg("CPF inválido, tente novamente")
        else:
            self.__tela_notificacao.mostra_msg("Ocorreu um erro ao adicionar uma notificacao, tente novamente")

    def remove_notificacao(self):
        self.listar_notificacoes()
        tipo = self.__tela_notificacao.seleciona_notificacao()
        notificacao = self.procura_notificacao_por_tipo(tipo)
        if notificacao is not None:
            self.__notificacoes.remove(notificacao)
            self.listar_notificacoes()

    def altera_notificacao(self):
        self.listar_notificacoes()
        tipo_notificacao = self.__tela_notificacao.seleciona_notificacao()
        notificacao = self.procura_notificacao_por_tipo(tipo_notificacao)
        if notificacao:
            novos_dados_notificacao = self.__tela_notificacao.pega_dados_notificacao()
            if self.__sistema.controlador_usuario.validar_cpf(novos_dados_notificacao["cpf"]):
                notificacao.tipo_notificacao = novos_dados_notificacao["tipo_notificacao"]
                notificacao.status = novos_dados_notificacao["status"]
                notificacao.usuario.cpf = novos_dados_notificacao["cpf"]
                notificacao.usuario.nome = novos_dados_notificacao["nome_usuario"]
            else:
                self.__tela_notificacao.mostra_msg("Cpf inválido, tente novamente")
        else:
            self.__tela_notificacao.mostra_msg("Ocorreu um erro ao alterar a notificacao, tente novamente")

    def procura_notificacao_por_tipo(self, tipo):
        for notificacao in self.__notificacoes:
            if notificacao.tipo_notificacao == tipo:
                return notificacao

    def listar_notificacoes(self):
        if self.__notificacoes:
            for notificacao in self.__notificacoes:
                self.__tela_notificacao.mostra_notificacao({"tipo_notificacao": notificacao.tipo_notificacao,
                                                            "status": notificacao.status,
                                                            "nome_usuario": notificacao.usuario.nome,
                                                            "cpf": notificacao.usuario.cpf})
        else:
            self.__tela_notificacao.mostra_msg("A lista de notificacoes está vazia :(")

    def validar_cpf(cpf):
        if not cpf.isdigit():
            raise ValueError("CPF deve ser composto apenas por números.")
        if len(cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos.")
        if cpf == cpf[0] * len(cpf):
            raise ValueError("CPF inválido: Todos os dígitos são iguais.")
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = 11 - soma % 11
        digito1 = digito1 if digito1 < 10 else 0
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = 11 - soma % 11
        digito2 = digito2 if digito2 < 10 else 0
        if cpf[-2:] != f"{digito1}{digito2}":
            raise ValueError("CPF incorreto: Dígitos verificadores inválidos.")
        return cpf

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.listar_notificacoes,
                        2: self.inclui_notificacao,
                        3: self.altera_notificacao,
                        4: self.remove_notificacao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_notificacao.tela_opcoes()]()
