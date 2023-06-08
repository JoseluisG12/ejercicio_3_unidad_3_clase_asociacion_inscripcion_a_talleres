import numpy as np
from Clase_inscipcion import Inscripcion
import csv
class Arreglo_inscripciones:
    __cantidad = 0
    __dimencion = 0
    __incremento = 1
    __punyod = None

    def __init__(self,dimencion,incremento = 5) ->None:
        self.inscripciones = np.empty(dimencion,dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimencion = dimencion

    def agregarinscripcion(self,unainscripcion):
        if self.__cantidad == self.__dimencion:
            self.__dimencion += self.__incremento
            self.inscripciones.resize(self.__dimencion,refcheck=False)
        self.inscripciones[self.__cantidad] = unainscripcion
        self.__cantidad += 1

    def buscardni(self):
        dni = int(input("ingrese el dni a buscar\n"))
        band = True
        i = 0
        while band and i < len(self.inscripciones):
            if self.inscripciones[i].getpersona().getdni() == dni:
                band = False
            else:
                i = i + 1
        if band:
            print("no se contro inscripto")
        else:
            return i
    def mostrarincripto(self):
        indice = self.buscardni()
        if indice == None:
            print("Error")
        else:

            print(f"""
se encontro un inscripto en {self.inscripciones[indice].gettaller().getnombre()} su monto adeudado es: ${self.inscripciones[indice].gettaller().getmonto()}""")

    def buscartaller(self,id):
        band = True
        i = 0
        while band and i < len(self.inscripciones):
            if self.inscripciones[i].gettaller().getid() == id:
                band = False
            else:
                i = i + 1
        if band:
            print("no se contro el taller")
        else:
            return i

    def mostrarinscritosxtaller(self):
        id = int(input("ingrese el id del taller a buscar sus inscriptos\n"))
        indice = self.buscartaller(id)
        print(f"""
{self.inscripciones[indice].gettaller().getnombre()}""")
        for i in  range(len(self.inscripciones)):
            if self.inscripciones[i] is not None and self.inscripciones[i].gettaller() is not None:
                taller = self.inscripciones[i].gettaller()
                if taller.getid() == id:
                    print(str(self.inscripciones[i].getpersona()))



    def registrapago(self):
        indice = self.buscardni()
        self.inscripciones[indice].actualizarpago()

    def crearcsv(self):
        nombre_archivo = input('ingrese nombre del archivo: \n')
        nombre_archivo += '.csv'
        encabezados = ['DNI', 'idTaller', 'fechaInscripcion', 'pago']
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=';')
            writer.writerow(encabezados)
            for inscripcion in self.inscripciones:
                if inscripcion is not None and inscripcion.getpersona() is not None:
                    dato = [inscripcion.getpersona().getdni(), inscripcion.gettaller().getid(), inscripcion.getfecha(),
                            inscripcion.getpago()]
                    writer.writerow(dato)
        print(f"Se ha generado el archivo CSV '{nombre_archivo}' con éxito.")




