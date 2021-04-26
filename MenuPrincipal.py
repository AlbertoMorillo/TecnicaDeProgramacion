from CarreraHome import CarrHome
from SeleccionEstudiante import SeleccionHome
from SeleccionProfesor import SeleccionProfesorHome
from MateriaHome import MateriaHome
from PensumHome import PensumHome
from EstudianteHome import EstudianteHome
from ProfesorHome import ProfesorHome

class MenuPrincipal:
    @staticmethod
    def Menu():
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("\n################## Menu principal ###################")
            print("1 ##### Menu Carrera ####")
            print("2 ##### Menu Seleccion estudiante ####")
            print("3 ##### Menu Seleccion profesor ####")
            print("4 ##### Menu Estudiante ####")
            print("5 ##### Menu Profesor ####")
            print("6 ##### Menu Pensum ####")
            print("7 ##### Menu Materia ####")
            print("8 ##### Salir ####")
            print("#######################\n")
            opcion = int(input("Selecciona una opcion: "))

            if opcion < 1 or opcion > 8:
                print("Opcion incorrecta, ingrese nuevamente.")
            elif opcion == 8:
                opcionCorrecta = True
                print("\nNos vemos pronto!\n")
                break
            else:
                opcionCorrecta = True
                MenuPrincipal().ejecutarOpcion(opcion)

    @staticmethod
    def ejecutarOpcion(opcion):
        if opcion == 1:
            CarrHome()
        elif opcion == 2:
            SeleccionHome()
        elif opcion == 3:
            SeleccionProfesorHome()
        elif opcion == 4:
            EstudianteHome()
        elif opcion == 5:
            ProfesorHome()
        elif opcion == 6:
            PensumHome()
        elif opcion == 7:
            MateriaHome()


MenuPrincipal().Menu()