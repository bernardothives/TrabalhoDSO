from entidade.localizacao_entidade import Localizacao


class LocalizacaoControle:

    def __init__(self):
        self.__tela_localizacao = None
        self.__localizacoes = []

    def inclui_localizacao(self, localizacao):
        if isinstance(localizacao, Localizacao):
            if localizacao not in self.__localizacoes:
                self.__localizacoes.append(localizacao)

    def altera_localizacao(self, cidade, novacidade):
        for localizacao in self.__localizacoes:
            if localizacao.cidade == cidade:
                localizacao.cidade(novacidade)

    def remove_localizacao(self, localizacao):
        if isinstance(localizacao, Localizacao):
            if localizacao in self.__localizacoes:
                self.__localizacoes.remove(localizacao)

    @property
    def listar_localizacoes(self):
        return self.__localizacoes
