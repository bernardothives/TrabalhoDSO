

class Localizacao:

    def __init__(self, cidade):
        self.__cidade = cidade

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade