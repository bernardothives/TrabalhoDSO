from clima_entidade_abstrata import ClimaEntidadeAbstrata


class ClimaPrevisaoEntidade(ClimaEntidadeAbstrata):

    def __init__(self, temperatura: int, humidade: int,
                 velocidade_vento: int, volume_chuva: int,
                 visibilidade: int, sensacao_termica: int,
                 data: str, descricao: str):
        super().__init__(temperatura, humidade,
                         velocidade_vento, volume_chuva,
                         visibilidade, sensacao_termica, data)
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
