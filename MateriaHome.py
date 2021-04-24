from conexionMateria import MateriaDAO
import funcionesMateria

def MateriaHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar materias ####")
            print("2 ##### Registrar materias ####")
            print("3 ##### Actualizar materias ####")
            print("4 ##### Eliminar materias ####")
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
    dao = MateriaDAO()

    if opcion == 1:
        try:
            materia = dao.listarMaterias()
            if len(materia) > 0:
                funciones.listarMaterias(materia)
            else:
                print("No se encuentran cursos")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        materia = funciones.pedirDatosRegistro()
        try:
            dao.registrarMateria(materia)
        except:
            print("Ocurrio un error.")
    elif opcion == 3:
        materia = dao.listarMaterias()
        if len(materia) > 0:
            curso = funciones.pedirDatosActualizacion(materia)
            if curso:
                dao.actualizarMateria(curso)
            else:
                print("Codigo de materia no encontrado.")
    elif opcion == 4:
        try:
            materia = dao.listarMaterias()
            if len(materia) > 0:
                codigoEleminar = funciones.pedirDatosEliminacion(materia)
                if not(codigoEleminar == ""):
                    dao.eliminarMateria(codigoEleminar)
                else:
                    print("Codigo de materia no encontrado.")
            else:
                print("No se encontro materia.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")


MateriaHome()

    