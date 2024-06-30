class CpfNaoEhNumero(Exception):
    def __init__(self):
        super().__init__("CPF deve ser composto apenas por números.")