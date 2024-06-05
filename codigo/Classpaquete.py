
class Paquete:
    __nroenv: int
    __peso: float
    __nomdest: str
    __dirdest:str
    __entregado: bool
    __observacion:str
    __idpaq: int
    
    def __init__(self, nroenv, peso, nomdest, dirdest, entregado, observacion, idpaq):
        self.__nroenv = nroenv
        self.__peso = peso
        self.__nomdest = nomdest
        self.__dirdest = dirdest
        self.__entregado = entregado
        self.__observacion = observacion
        self.__idpaq = idpaq
        
    def __str__(self):
        return f"NROENV: {self.__nroenv} PESO: {self.__peso} NOMDEST: {self.__nomdest} DIRDEST: {self.__dirdest} ENTREGADO: {self.__entregado} OBSERVACION: {self.__observacion}"
    def getnroenv(self):
        return self.__nroenv
    def getpeso(self):
        return self.__peso
    def getnomdest(self):
        return self.__nomdest
    def getdirdest(self):
        return self.__dirdest
    def getentregado(self):
        return self.__entregado
    def getobservacion(self):
        return self.__observacion
    def getidpaq(self):
        return self.__idpaq
