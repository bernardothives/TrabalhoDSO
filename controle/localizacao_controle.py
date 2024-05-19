from entidade.localizacao_entidade import Localizacao
from limite.localizacao_tela import LocalizacaoTela


class LocalizacaoControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__tela_localizacao = LocalizacaoTela()
        self.__localizacoes = []

    def procura_localizacao_por_cidade(self, cidade):
        for localizacao in self.__localizacoes:
            if localizacao.cidade == cidade:
                return localizacao

    def inclui_localizacao(self):
        dados_localizacao = self.__tela_localizacao.pergunta_cidade()
        localizacao = Localizacao(dados_localizacao)
        self.__localizacoes.append(localizacao)

    def altera_localizacao(self):
        self.listar_localizacoes()
        cidade = self.__tela_localizacao.seleciona_cidade()
        localizacao = self.procura_localizacao_por_cidade(cidade)
        if localizacao is not None:
            novos_dados_localizacao = self.__tela_localizacao.pergunta_cidade()
            localizacao.cidade = novos_dados_localizacao

    def remove_localizacao(self):
        self.listar_localizacoes()
        cidade = self.__tela_localizacao.seleciona_cidade()
        localizacao = self.procura_localizacao_por_cidade(cidade)
        if localizacao in self.__localizacoes:
            self.__localizacoes.remove(localizacao)
            self.listar_localizacoes()

    def listar_localizacoes(self):
        for localizacao in self.__localizacoes:
            self.__tela_localizacao.mostra_cidades({"cidade": localizacao.cidade})

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_localizacao,
                        2: self.altera_localizacao,
                        3: self.listar_localizacoes,
                        4: self.remove_localizacao,
                        0: self.retornar}
