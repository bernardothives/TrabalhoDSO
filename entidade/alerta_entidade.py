

class Alerta:

    def __init__(self, tipo_alerta: str, severidade: str):
        self.__tipo_alerta = tipo_alerta
        self.__severidade = severidade

    @property
    def tipo_alerta(self):
        return self.__tipo_alerta

    @tipo_alerta.setter
    def tipo_alerta(self, tipo_alerta):
        self.__tipo_alerta = tipo_alerta

    @property
    def severidade(self):
        return self.__severidade

    @severidade.setter
    def severidade(self, severidade):
        self.__severidade = severidade
