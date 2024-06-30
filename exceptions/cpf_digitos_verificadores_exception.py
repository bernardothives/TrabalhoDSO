class CpfDigitosVerificadores(Exception):
    def __init__(self):
        super().__init__("CPF incorreto: Dígitos verificadores inválidos.")