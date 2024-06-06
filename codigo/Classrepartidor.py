class Repartidor:
    __id: int
    __nombre: str
    __numero: int
    __dni: str
    
    def __init__(self, nombre, numero, dni, id):
        self.__nombre = nombre
        self.__numero = numero
        self.__dni = dni
        self.__id = id
        
    def getNombre(self):
        return self.__nombre
    
    def getNumero(self):
        return self.__numero
    
    def getDni(self):
        return self.__dni
    def getId(self):
        return self.__id
    
    def __str__(self):
        return f"Repartidor {self.__nombre} {self.__numero} {self.__dni} {self.__id}"