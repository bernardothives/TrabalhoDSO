from entidade.alerta_entidade import Alerta
from limite.alerta_tela import AlertaTela


class AlertaControle:

    def __init__(self, controlador_previsao):
        self.__controlador_previsao = controlador_previsao
        self.__alerta_tela = AlertaTela()
        self.__alertas = []

    def inclui_alerta(self, tipo_alerta, severidade):
        novoalerta = Alerta(tipo_alerta, severidade)
        if novoalerta not in self.__alertas:
            self.__alertas.append(novoalerta)

    def altera_alerta(self, alerta, tipo_alerta, severidade):
        if isinstance(alerta, Alerta):
            if alerta in self.__alertas:
                alerta.tipo_alerta = tipo_alerta
                alerta.severidade = severidade

    def remove_alerta(self, alerta):
        if isinstance(alerta, Alerta):
            if alerta in self.__alertas:
                self.__alertas.remove(alerta)

    @property
    def listar_alertas(self):
        return self.__alertas

    def procura_alerta_por_tipo(self, tipo_alerta):
        lista_por_tipos = []
        for alerta in self.__alertas:
            if alerta.tipo_alerta == tipo_alerta:
                lista_por_tipos.append(alerta)
        return lista_por_tipos

    def retornar(self):
        self.__controlador_previsao.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_alerta, 2: self.altera_alerta,
                        3: self.remove_alerta, 0: self.retornar}

        while True:
            opcao_escolhida = self.__alerta_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
