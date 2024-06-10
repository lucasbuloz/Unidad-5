class Paquete:
    __id: int
    __numeroEnvio: int
    __peso: int
    __nombreDestinatario: str
    __direccionDestinatario: str
    __entregado: bool
    __observaciones: str
    __repartidor: list
    __transporte: list
    __sucursal: list
    
    def __init__(self, numeroEnvio, peso, nombreDestinatario, direccionDestinatario, entregado, observaciones, id):
        self.__numeroEnvio = numeroEnvio
        self.__peso = peso
        self.__nombreDestinatario = nombreDestinatario
        self.__direccionDestinatario = direccionDestinatario
        self.__entregado = entregado
        self.__observaciones = observaciones
        self.__id = id
        
    def setRepartidor(self, repartidor):
        self.__repartidor.append(repartidor)
    
    def setTransporte(self, transporte):
        self.__transporte.append(transporte)
    
    def setSucursal(self, sucursal):
        self.__sucursal.append(sucursal)
    
    def getNumeroEnvio(self):
        return self.__numeroEnvio
    
    def getPeso(self):
        return self.__peso
    
    def getNombreDestinatario(self):
        return self.__nombreDestinatario
    
    def getDireccionDestinatario(self):
        return self.__direccionDestinatario
    
    def getEntregado(self):
        return self.__entregado
    
    def getObservaciones(self):
        return self.__observaciones
    def getId(self):
        return self.__id
    
    def __str__(self): 
        return f"Paquete {self.__numeroEnvio} {self.__peso} {self.__nombreDestinatario} {self.__direccionDestinatario} {self.__entregado} {self.__observaciones} {self.__id}"
    