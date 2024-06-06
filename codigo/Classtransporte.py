from datetime import datetime

class Transporte:
    __id: int
    __numeroTransporte = int
    __fechaHoraSaida = datetime
    __fechaHoraLLegada = datetime
    
    def __init__(self, numeroTransporte, fechaHoraSaida, fechaHoraLLegada, id):
        self.__id = id
        self.__numeroTransporte = numeroTransporte
        self.__fechaHoraSaida = fechaHoraSaida
        self.__fechaHoraLLegada = fechaHoraLLegada

    def getNumeroTransporte(self):
        return self.__numeroTransporte

    def getFechaHoraSaida(self):
        return self.__fechaHoraSaida

    def getFechaHoraLLegada(self):
        return self.__fechaHoraLLegada
    
    def getId(self):
        return self.__id
    
    def __str__(self):
        return f"Transporte {self.__numeroTransporte} {self.__fechaHoraSaida} {self.__fechaHoraLLegada} {self.__id}"