
class Inscripcion:
    __fecha : str
    __pago : bool
    __persona : object
    __taller : object

    def __init__(self,fecha,pago,persona,taller):
        self.__fecha = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def getpersona(self):
        return self.__persona

    def getpago(self):
        return self.__pago

    def getfecha(self):
        return self.__fecha

    def actualizarpago(self):
        self.__pago = True

    def gettaller(self):
        return self.__taller

    def __str__(self):
        return f"""
fecha:{self.__fecha}
inscripto:{self.__persona}
taller:{self.__taller}"""