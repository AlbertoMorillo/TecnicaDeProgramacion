from conexionEstudiante import EstudianteDAO
from conexionCarrera import CarreraDAO
import funcionesEstudiante
import funcionesCarrera

def EstudianteHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar estudiantes ####")
            print("2 ##### Registrar estudiantes ####")
            print("3 ##### Actualizar estudiantes ####")
            print("4 ##### Eliminar estudiantes ####")
            print("5 ##### Salir ####")
            print("#######################")
            opcion = int(input("Selecciona una opcion: "))
    
            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, ingrese nuevamente.")
            elif opcion == 5:
                continuar = False
                print("\nNos vemos pronto!\n")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = EstudianteDAO()
    daoCarr = CarreraDAO()

    if opcion == 1:
        try:
            estudiante = dao.listarEstudiantes()
            if len(estudiante) > 0:
                funcionesEstudiante.listarEstudiantes(estudiante)
            else:
                print("No se encuentran estudiantes\n")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        print("\nA continuacion, listado de carreras a elegir: ")
        carrera = daoCarr.listarCarreras()
        if len(carrera) > 0:
            funcionesCarrera.listarCarerras(carrera)
        else:
            print("No se encuentran materias")
        estudiante = funcionesEstudiante.pedirDatosRegistro()
        try:
            dao.registrarEstudiante(estudiante)
        except:
            print("Ocurrio un error.")
    elif opcion == 3:
        estudiante = dao.listarEstudiantes()
        if len(estudiante) > 0:
            est = funcionesEstudiante.pedirDatosActualizacion(estudiante)
            if est:
                dao.actualizarEstudiante(est)
            else:
                print("Matricula de estudiante no encontrado.")
    elif opcion == 4:
        try:
            estudiante = dao.listarEstudiantes()
            if len(estudiante) > 0:
                codigoEleminar = funcionesEstudiante.pedirDatosEliminacion(estudiante)
                if not(codigoEleminar == ""):
                    dao.eliminarEstudiante(codigoEleminar)
                else:
                    print("Codigo de estudiante no encontrado.")
            else:
                print("No se encontro estudiante.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")


EstudianteHome()

    