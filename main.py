from Clase_Menu import Menu
import csv
from Manejador_talleres import Arreglos_Talleres
from Manejador_Personas import Lista_Personas
from Manejador_inscripciones import Arreglo_inscripciones
if __name__=='__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        next(reader)
        primera_fila = next(reader)
        Mtalleres = Arreglos_Talleres(int(primera_fila[0]))
        Mtalleres.cargadatos()
        Mpersonas = Lista_Personas()
        Minscripciones = Arreglo_inscripciones(2)
        Mtalleres .test(Mpersonas,Minscripciones)
    print("_____main_____")
    archivo = open('Talleres.csv')
    reader = csv.reader(archivo,delimiter=(';'))
    next(reader)
    primera_fila = next(reader)
    talleres = Arreglos_Talleres(int(primera_fila[0]))
    talleres.cargadatos()
    personas = Lista_Personas()
    inscripciones = Arreglo_inscripciones(5)
    menu = Menu()
    menu.run(talleres,personas,inscripciones)


