
class Repartidor:
    __nro: int
    __nom: str
    __dni: str
    __idrep: int
    
    def __init__(self, nro, nom, dni, idrep):
        self.__nro = nro
        self.__nom = nom
        self.__dni = dni        
        self.__idrep = idrep
        
    def __str__(self):
        return f"NRO: {self.__nro} NOM: {self.__nom} DNI: {self.__dni}"
    def getnro(self):
        return self.__nro
    def getnom(self):
        return self.__nom
    def getdni(self):
        return self.__dni
    def getidrep(self):
        return self.__idrep