from conexionPensum import PensumDAO
from conexionCarrera import CarreraDAO
from conexionMateria import MateriaDAO
import funcionesPensum
import funcionesCarrera
import funcionesMateria

def PensumHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar pensums ####")
            print("2 ##### Registrar pensums ####")
            print("3 ##### Actualizar pensums ####")
            print("4 ##### Eliminar pensums ####")
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
    dao = PensumDAO()
    daoCarr = CarreraDAO()
    daoMat = MateriaDAO()

    if opcion == 1:
        try:
            pensum = dao.listarPensums()
            if len(pensum) > 0:
                funcionesPensum.listarPensums(pensum)
            else:
                print("No se encuentran pensums\n")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        print("\nA continuacion, listado de carreras a elegir: ")
        carrera = daoCarr.listarCarreras()
        if len(carrera) > 0:
            funcionesCarrera.listarCarerras(carrera)
        else:
            print("No se encuentran carreras")
        
        print("\nA continuacion, listado de materias a elegir: ")
        materia = daoMat.listarMaterias()
        if len(carrera) > 0:
            funcionesMateria.listarMaterias(materia)
        else:
            print("No se encuentran materias")
        pensum = funcionesPensum.pedirDatosRegistro()
        try:
            dao.registrarPensum(pensum)
        except:
            print("Ocurrio un error.")
    elif opcion == 3:
        pensum = dao.listarPensums()
        if len(pensum) > 0:
            pen = funcionesPensum.pedirDatosActualizacion(pensum)
            if pen:
                dao.actualizarPensum(pen)
            else:
                print("ID de pensum no encontrado.")
    elif opcion == 4:
        try:
            pensum = dao.listarPensums()
            if len(pensum) > 0:
                codigoEleminar = funcionesPensum.pedirDatosEliminacion(pensum)
                if not(codigoEleminar == ""):
                    dao.eliminarPensum(codigoEleminar)
                else:
                    print("Codigo de pensum no encontrado.")
            else:
                print("No se encontro pensum.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")




    