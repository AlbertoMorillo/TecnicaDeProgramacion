from conexionProfesor import ProfesorDAO
import funcionesProfesor

def ProfesorHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar profesores ####")
            print("2 ##### Registrar profesores ####")
            print("3 ##### Actualizar profesores ####")
            print("4 ##### Eliminar profesores ####")
            print("5 ##### Salir ####")
            print("#######################")
            opcion = int(input("Selecciona una opcion: "))
    
            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, ingrese nuevamente.")
            elif opcion == 5:
                continuar = False
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = ProfesorDAO()

    if opcion == 1:
        try:
            profesor = dao.listarProfesors()
            if len(profesor) > 0:
                funcionesProfesor.listarProfesores(profesor)
            else:
                print("No se encuentran profesores\n")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        profesor = funcionesProfesor.pedirDatosRegistro()
        try:
            dao.registrarProfesor(profesor)
        except:
            print("Ocurrio un error.\n")
    elif opcion == 3:
        profesor = dao.listarProfesors()
        if len(profesor) > 0:
            carr = funcionesProfesor.pedirDatosActualizacion(profesor)
            if carr:
                dao.actualizarProfesor(carr)
            else:
                print("Nombre de profesor no encontrado.\n")
    elif opcion == 4:
        try:
            profesor = dao.listarProfesors()
            if len(profesor) > 0:
                codigoEleminar = funcionesProfesor.pedirDatosEliminacion(profesor)
                if not(codigoEleminar == ""):
                    dao.eliminarProfesor(codigoEleminar)
                else:
                    print("Nombre de profesor no encontrado.")
            else:
                print("No se encontro profesor.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")




    