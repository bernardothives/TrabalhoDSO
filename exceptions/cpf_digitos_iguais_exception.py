class CpfDigitosIguais(Exception):
    def __init__(self):
        super().__init__("CPF inválido: Todos os dígitos são iguais.")