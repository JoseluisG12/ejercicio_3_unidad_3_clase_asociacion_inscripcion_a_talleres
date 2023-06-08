
class Menu:
    __switcher = None

    def __init__(self)->None:
        self.__switcher = {1:self.op1,
                           2:self.op2,
                           3:self.op3,
                           4:self.op4,
                           5:self.op5,
                           }


    def run(self,talleres,personas,inscripciones):
        band = True
        while band:
            b = int(input("""
Menu Principal:
1-incribir a una persona en un taller
2-buscar inscripto por dni
3-conocer inscriptos por id de taller
4-registra pago
5-cargar inscriptos
\n"""))
            func = self.__switcher.get(b)
            if func:
                func(talleres,personas,inscripciones)
            else:
                print("Saliendo...")
                band = False

    def op1(self,talleres,personas,inscripciones):
        talleres.inscribirpersona(personas,inscripciones)

    def op2(self,talleres,personas,inscripciones):
        inscripciones.mostrarincripto()

    def op3(self,talleres,personas,inscripciones):
        inscripciones.mostrarinscritosxtaller()

    def op4(self,talleres,personas,inscripciones):
        inscripciones.registrapago()

    def op5(self,talleres,personas,inscripciones):
        inscripciones.crearcsv()
