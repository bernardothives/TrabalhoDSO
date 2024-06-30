class CpfTamanhoErrado(Exception):
    def __init__(self):
        super().__init__("CPF deve conter 11 dígitos.")