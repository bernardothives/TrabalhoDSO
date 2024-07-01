class LocalizacaoDuplicada(Exception):
    def __init__(self):
        super().__init__("Localização já cadastrada")