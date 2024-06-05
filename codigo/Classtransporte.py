from datetime import datetime
from typing import Any

class Transporte:
    __nrotrans: int
    __fechaHoraSalida: datetime
    __fechaHoraLlegada: datetime
    __idtrans: int
    
    def __init__(self, nrotrans, fechaHoraSalida, fechaHoraLlegada, idtrans):
        self.__nrotrans = nrotrans
        self.__fechaHoraSalida = fechaHoraSalida
        self.__fechaHoraLlegada = fechaHoraLlegada    
        self.__idtrans = idtrans
    
    def getNrotrans(self):
        return self.__nrotrans
    def getFechaHoraSalida(self):
        return self.__fechaHoraSalida
    def getFechaHoraLlegada(self):
        return self.__fechaHoraLlegada
    def getIdtrans(self):
        return self.__idtrans
    
    def __str__(self):
        return f"NROTRANS: {self.__nrotrans}, FECHA HORA SALIDA: {self.__fechaHoraSalida}, FECHA HORA Llegada: {self.__fechaHoraLlegada}"
    