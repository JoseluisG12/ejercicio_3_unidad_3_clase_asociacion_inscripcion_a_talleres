
class Persona:
    __nombre : str
    __direccion : str
    __dni : int

    def __init__(self,nombre,direccion,dni)->None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def getdni(self):
        return self.__dni

    def getnombre(self):
        return self.__nombre




    def __str__(self):
        return f"""
nombre:{self.__nombre}
DNI {self.__dni}"""