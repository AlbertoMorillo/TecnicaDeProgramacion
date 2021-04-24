from conexionCarrera import CarreraDAO
import funcionesCarrera

def CarreraHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar carreras ####")
            print("2 ##### Registrar carreras ####")
            print("3 ##### Actualizar carreras ####")
            print("4 ##### Eliminar carreras ####")
            print("5 ##### Salir ####")
            print("#######################")
            opcion = int(input("Selecciona una opcion"))
    
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
    dao = CarreraDAO()

    if opcion == 1:
        try:
            carrera = dao.listarCarreras()
            if len(carrera) > 0:
                funciones.listarCaterias(carrera)
            else:
                print("No se encuentran cursos")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        carrera = funciones.pedirDatosRegistro()
        try:
            dao.registrarCarrera(carrera)
        except:
            print("Ocurrio un error.")
    elif opcion == 3:
        carrera = dao.listarCarreras()
        if len(carrera) > 0:
            curso = funciones.pedirDatosActualizacion(carrera)
            if curso:
                dao.actualizarCarrera(curso)
            else:
                print("Codigo de carrera no encontrado.")
    elif opcion == 4:
        try:
            carrera = dao.listarCarreras()
            if len(carrera) > 0:
                codigoEleminar = funciones.pedirDatosEliminacion(carrera)
                if not(codigoEleminar == ""):
                    dao.eliminarCarrera(codigoEleminar)
                else:
                    print("Codigo de carrera no encontrado.")
            else:
                print("No se encontro carrera.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")


CarreraHome()

    