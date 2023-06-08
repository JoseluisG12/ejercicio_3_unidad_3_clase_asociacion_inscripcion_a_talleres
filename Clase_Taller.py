
class Taller:
    __id : int
    __nombre : str
    __vacantes : int
    __monto : float
    __inscipciones : list

    def __init__(self,id,nombre,vacante,monto)-> None:
        self.__id = int(id)
        self.__nombre = nombre
        self.__vacantes = vacante
        self.__monto = monto
        self.__inscipciones = []

    def getnombre(self):
        return self.__nombre

    def getvacantes(self):
        return self.__vacantes

    def getmonto(self):
        return self.__monto

    def getid(self):
        return self.__id

    def addinscipcion(self,inscripcion):
        self.__inscipciones.append(inscripcion)

    def mostrarinscripcion(self):
        for i in range(len(self.__inscipciones)):
            print(str(self.__inscipciones[i]))

    def actualizarvacante(self):
        self.__vacantes = self.__vacantes - 1

    def __str__(self)-> str:
        return f"""
taller :{self.__id}° 
nombre:{self.__nombre}
vacantes:{self.__vacantes}
monto:{self.__monto}"""



