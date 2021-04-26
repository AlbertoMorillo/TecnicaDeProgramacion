from conexionSeleccion import SeleccionDAO
from conexionEstudiante import EstudianteDAO
from conexionMateria import MateriaDAO
import funcionesSeleccion
import funcionesEstudiante
import funcionesMateria

def SeleccionHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar seleccion ####")
            print("2 ##### Registrar seleccion ####")
            print("3 ##### Actualizar seleccion ####")
            print("4 ##### Eliminar seleccion ####")
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
    dao = SeleccionDAO()
    daoEst = EstudianteDAO()
    daoMat = MateriaDAO()

    if opcion == 1:
        try:
            seleccion = dao.listarSeleccions()
            if len(seleccion) > 0:
                funcionesSeleccion.listarSeleccions(seleccion)
            else:
                print("No se encuentran seleccions\n")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        print("\nA continuacion, listado de estudiantes a elegir: ")
        estu = daoEst.listarEstudiantes()
        if len(estu) > 0:
            funcionesEstudiante.listarEstudiantes(estu)
        else:
            print("No se encuentran estu")
        
        print("\nA continuacion, listado de materias a elegir: ")
        materia = daoMat.listarMaterias()
        if len(materia) > 0:
            funcionesMateria.listarMaterias(materia)
        else:
            print("No se encuentran materias")
        seleccion = funcionesSeleccion.pedirDatosRegistro()
        try:
            dao.registrarSeleccion(seleccion)
        except:
            print("Ocurrio un error.")
    elif opcion == 3:
        seleccion = dao.listarSeleccions()
        if len(seleccion) > 0:
            sel = funcionesSeleccion.pedirDatosActualizacion(seleccion)
            if sel:
                dao.actualizarSeleccion(sel)
            else:
                print("ID de seleccion no encontrado.")
    elif opcion == 4:
        try:
            seleccion = dao.listarSeleccions()
            if len(seleccion) > 0:
                codigoEleminar = funcionesSeleccion.pedirDatosEliminacion(seleccion)
                if not(codigoEleminar == ""):
                    dao.eliminarSeleccion(codigoEleminar)
                else:
                    print("Codigo de seleccion no encontrado.")
            else:
                print("No se encontro seleccion.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")



    