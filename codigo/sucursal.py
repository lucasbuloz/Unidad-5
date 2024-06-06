class Sucursal:
    __id: int
    __numero: int
    __provincia: str
    __localidad: str
    __direccion: str
    
    def __init__(self, numero, provincia, localidad, direccion, id):
        self.__id = id
        self.__numero = numero
        self.__provincia = provincia
        self.__localidad = localidad
        self.__direccion = direccion
        
    def getNumero(self):
        return self.__numero
    
    def getProvincia(self):
        return self.__provincia
    
    def getLocalidad(self):
        return self.__localidad
    
    def getDireccion(self):
        return self.__direccion
    
    def getId(self):
        return self.__id
    
    def __str__(self):
        return f"Sucursal {self.__numero} {self.__provincia} {self.__localidad} {self.__direccion} {self.__id}"