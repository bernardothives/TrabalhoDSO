from limite.alerta_tela import AlertaTela


class AlertaControle:

    def __init__(self, controlador_previsao):
        self.__controlador_previsao = controlador_previsao
        self.__alerta_tela = AlertaTela()

    def ver_alerta(self):
        self.__controlador_previsao.sistema.controlador_localizacao.listar_localizacoes()
        cidade = self.__alerta_tela.seleciona_cidade()
        localizacao = self.__controlador_previsao.sistema.controlador_localizacao.procura_localizacao_por_cidade(cidade)
        clima_id = self.__controlador_previsao.procura_id_clima_previsao_por_localizacao(localizacao)
        clima = self.__controlador_previsao.procura_clima_previsao_por_id(clima_id)
        print("haha")
        if clima:
            print("haha")
            if clima.velocidade_vento > 80:
                self.__alerta_tela.mostra_msg("CUIDADO: O vento nesta localizacao esta muito forte!")
            if clima.volume_chuva > 50:
                self.__alerta_tela.mostra_msg("CUIDADO: O volume de chuva nesta localizacao esta muito alto!")
            if clima.temperatura > 40:
                self.__alerta_tela.mostra_msg("CUIDADO: A temperatura nesta localizacao esta muito alta!")
            if clima.temperatura < -20:
                self.__alerta_tela.mostra_msg("CUIDADO: O temperatura nesta localizacao esta muito baixa!")

    def retornar(self):
        self.__controlador_previsao.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_alerta, 0: self.retornar}

        while True:
            opcao_escolhida = self.__alerta_tela.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
