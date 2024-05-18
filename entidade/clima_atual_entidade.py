from entidade.clima_entidade_abstrata import ClimaEntidadeAbstrata


class ClimaAtualEntidade(ClimaEntidadeAbstrata):
    def __init__(self, temperatura: int, humidade: int,
                 velocidade_vento: int, volume_chuva: int,
                 visibilidade: int, sensacao_termica: int,
                 data: str, horario: str):
        super().__init__(temperatura, humidade,
                         velocidade_vento, volume_chuva,
                         visibilidade, sensacao_termica, data)
        if isinstance(horario, str):
            self.__horario = horario

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        if isinstance(horario, str):
            self.__horario = horario
