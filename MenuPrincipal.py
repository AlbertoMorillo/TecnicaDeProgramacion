from CarreraHome import CarrHome
from SeleccionEstudiante import SeleccionHome
from SeleccionProfesor import SeleccionProfesorHome
from MateriaHome import MateriaHome
from PensumHome import PensumHome
from EstudianteHome import EstudianteHome
from ProfesorHome import ProfesorHome
import mysql.connector
from mysql.connector import Error

class MenuPrincipal:
    def Menu(self):
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

    def ejecutarOpcion(self,opcion):
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

    def login(self):
        try:
            self.conexion = mysql.connector.connect(
                host= 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'universidad'
            )
        except Error as ex:
            print("Error al internar la conexion {0}".format(e))
        
        user = input("Ingrese el usuario: ")
        passw = input("Ingrese el password: ")

        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT * FROM credenciales WHERE usuario = '{0}' AND password = '{1}'"
                cursor.execute(sql.format(user,passw))
                resultados = cursor.fetchall()
                if resultados:
                    return True
                else:
                    return False
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            return False

    def main(self):
        log = MenuPrincipal().login()
        if log == True:
            MenuPrincipal().Menu()
        else:
            print("Usuario o contraseña invalida.")


MenuPrincipal().main()