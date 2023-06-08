import numpy as np
from Clase_Taller import Taller
from Clase_Persona import Persona
from Clase_inscipcion import Inscripcion
import  csv
from datetime import datetime
class  Arreglos_Talleres:
    __cantidad  = 0
    __dimencion = 0
    __incremento = 5
    __punyod = None

    def __init__(self,dimencion,incremento = 5) -> None:
        self.Talleres = np.empty(dimencion,dtype=Taller)
        self.__cantidad = 0
        self.__dimencion = dimencion

    def agregartaller(self,untaller):
        if self.__cantidad == self.__dimencion:
            self.__dimencion += self.__incremento
            self.Talleres.resize(self.__dimencion, refcheck=False)
        self.Talleres[self.__cantidad] = untaller
        self.__cantidad += 1


    def cargadatos(self):
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo,delimiter=(';'))
        next(reader)
        next(reader)
        for fila in reader:
            self.agregartaller(Taller(int(fila[0]),fila[1],int(fila[2]),int(fila[3])))
        archivo.close()


    def mostrartalleres(self):
        for taller in self.gettaller():
            print(str(taller))

    def gettaller(self):
        return self.Talleres

    def buscartaller(self,taller):
        band = True
        i = 0
        while band and i < len(self.Talleres):
            if self.Talleres[i].getnombre() == taller:
                band = False
            else:
                i = i + 1
        if not band:
            return self.Talleres[i]
        else:
            print("Error no se encontro el taller")

    def inscribirpersona(self,M_persona,M_inscripcion):
        self.mostrartalleres()
        nombre_taller = input("ingrese el nombre del taller a inscribirse\n")
        taller = self.buscartaller(nombre_taller)
        if taller.getvacantes() > 0:
            nombre = input("ingrese el nombre de la persona\n")
            direccion = input("ingrese la direccion del inscripto\n")
            dni = int(input("ingrese el dni del inscripto\n"))
            b = input("desea abonar el pago al momento de la inscripcion y == si , n == no\n")
            if b == 'y':
                pago = True
            elif b == 'n':
                pago = False
            persona = Persona(nombre, direccion, dni)
            M_persona.addpersona(persona)
            inscripcion = Inscripcion(datetime.now().date(), pago, persona, taller)
            M_inscripcion.agregarinscripcion(inscripcion)
            taller.addinscipcion(inscripcion)
            taller.actualizarvacante()

    def mostrarinscripciones(self):
        for taller in self.Talleres:
            taller.mostrarinscripcion()

    def test(self,Mpersonas,Minscripciones):
        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
        while opc != 0:
            if opc == 1:
                print("_____inscribir_persona_____")
                self.mostrartalleres()
                nombre_taller = input("ingrese el nombre del taller a inscribirse\n")
                taller = self.buscartaller(nombre_taller)
                if taller.getvacantes() > 0:
                    nombre = 'juan'
                    direccion = 'av.coratina'
                    dni = 41230328
                    b = 'n'
                    if b == 'y':
                        pago = True
                    elif b == 'n':
                        pago = False
                    persona = Persona(nombre, direccion, dni)
                    Mpersonas.addpersona(persona)
                    inscripcion = Inscripcion(datetime.now().date(), pago, persona, taller)
                    Minscripciones.agregarinscripcion(inscripcion)
                    taller.addinscipcion(inscripcion)
                    taller.actualizarvacante()
                    self.mostrarinscripciones()
                print("______busca_inscripto_por_dni_____")
                Minscripciones.mostrarincripto()
                print("______buscar_insriptos_por_id_de_taller_____")
                Minscripciones.mostrarinscritosxtaller()
                print("________registra_pago____________")
                Minscripciones.registrapago()
                print("___cargar_inscriptos______________")
                Minscripciones.crearcsv()
            if opc == 2:
                print("_____inscribir_persona_____")
                self.mostrartalleres()
                nombre_taller = input("ingrese el nombre del taller a inscribirse\n")
                taller = self.buscartaller(nombre_taller)
                if taller.getvacantes() > 0:
                    nombre = 'juan'
                    direccion = 'av.coratina'
                    dni = '41230328'
                    b = 'n'
                    if b == 'y':
                        pago = True
                    elif b == 'n':
                        pago = False
                    persona = Persona(nombre, direccion, dni)
                    Mpersonas.addpersona(persona)
                    inscripcion = Inscripcion(datetime.now().date(), pago, persona, taller)
                    Minscripciones.agregarinscripcion(inscripcion)
                    taller.addinscipcion(inscripcion)
                    taller.actualizarvacante()
                    self.mostrarinscripciones()
                print("______busca_inscripto_por_dni_____")
                Minscripciones.mostrarincripto()
                print("______buscar_insriptos_por_id_de_taller_____")
                Minscripciones.mostrarinscritosxtaller()
                print("________registra_pago____________")
                Minscripciones.registrapago()
                print("___cargar_inscriptos______________")
                Minscripciones.crearcsv()












