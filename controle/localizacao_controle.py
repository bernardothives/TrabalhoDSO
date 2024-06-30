from entidade.localizacao import Localizacao
from limite.localizacao_tela import LocalizacaoTela
from DAOs.localizacao_dao import LocalizacaoDAO
from exceptions.usuario_duplicado_exception import UsuarioDuplicado


class LocalizacaoControle:
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__tela_localizacao = LocalizacaoTela()
        self.__localizacao_DAO = LocalizacaoDAO()

    def procura_localizacao_por_cidade(self, cidade):
        return self.__localizacao_DAO.get(cidade)

    def inclui_localizacao(self):
        try:
            dados_localizacao = self.__tela_localizacao.pega_dados_localizacao()
            if dados_localizacao:
                cidade = dados_localizacao['cidade']
                localizacao = self.procura_localizacao_por_cidade(cidade)
                if localizacao:
                    # implementar loc duplicada
                    raise UsuarioDuplicado()
                else:
                    localizacao = Localizacao(dados_localizacao['cidade'], dados_localizacao['estado'], dados_localizacao['pais'])
                    self.__localizacao_DAO.add(localizacao)
                    return localizacao
        except UsuarioDuplicado as e:
            self.__tela_localizacao.mostra_msg(str(e))


    def altera_localizacao(self):
        self.listar_localizacoes()
        lista_cidades = [localizacao.cidade for localizacao in self.__localizacoes]
        cidade = self.__tela_localizacao.seleciona_cidade(lista_cidades)
        localizacao = self.procura_localizacao_por_cidade(cidade)
        if localizacao:
            novos_dados_localizacao = self.__tela_localizacao.pega_dados_localizacao()
            for loc in self.__localizacoes:
                if loc.cidade == novos_dados_localizacao["cidade"] and loc != localizacao:
                    self.__tela_localizacao.mostra_msg("Cidade ja cadastrada \n")
                    break
            localizacao.cidade = novos_dados_localizacao["cidade"]
            localizacao.estado = novos_dados_localizacao["estado"]
            localizacao.pais = novos_dados_localizacao["pais"]

    def remove_localizacao(self):
        self.listar_localizacoes()
        cidade = self.__tela_localizacao.seleciona_cidade()
        localizacao = self.procura_localizacao_por_cidade(cidade)
        if localizacao is not None:
            self.__localizacao_DAO.remove(cidade)
            self.__tela_localizacao.mostra_msg("Localização excluida com sucesso")

    def listar_localizacoes(self):
        localizacoes = self.__localizacao_DAO.get_all()
        if not localizacoes:
            self.__tela_localizacao.mostra_msg("Nenhuma localização cadastrada")
        else:
            dados_localizacoes = []
            for loc in localizacoes:
                dados_loc = {"cidade": loc.cidade, "estado": loc.estado, "pais": loc.pais}
                dados_localizacoes.append(dados_loc)
                self.__tela_localizacao.mostra_dados_localizacao(dados_loc)

    def retornar(self):
        self.__sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_localizacao,
                        2: self.altera_localizacao,
                        3: self.listar_localizacoes,
                        4: self.remove_localizacao,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_localizacao.tela_opcoes()]()
