from entidade.alerta_entidade import Alerta


class AlertaControle:

    def __init__(self):
        self.__tela_alerta = None
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

