class NomeVazio(Exception):
    def __init__(self):
        super().__init__("Nome não pode estar vazio.")