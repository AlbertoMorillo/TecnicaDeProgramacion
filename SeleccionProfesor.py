from conexionSeleccionProf import SeleccionProfDAO
from conexionProfesor import ProfesorDAO
from conexionMateria import MateriaDAO
import funcionesSeleccionProf
import funcionesProfesor
import funcionesMateria

def SeleccionProfesorHome():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("##### Menu principal ####")
            print("1 ##### Listar seleccion profesor ####")
            print("2 ##### Registrar seleccion profesor ####")
            print("3 ##### Actualizar seleccion profesor ####")
            print("4 ##### Eliminar seleccion profesor ####")
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
    dao = SeleccionProfDAO()
    daoProf = ProfesorDAO()
    daoMat = MateriaDAO()

    if opcion == 1:
        try:
            seleccion = dao.listarSeleccionProfs()
            if len(seleccion) > 0:
                funcionesSeleccionProf.listarSeleccionProfs(seleccion)
            else:
                print("No se encuentran seleccion de profesor\n")
        except:
            print("Ocurrio un error.")
    elif opcion == 2:
        print("\nA continuacion, listado de profesores a elegir: ")
        prof = daoProf.listarProfesors()
        if len(prof) > 0:
            funcionesProfesor.listarProfesores(prof)
        else:
            print("No se encuentran profesores")
        
        print("\nA continuacion, listado de materias a elegir: ")
        materia = daoMat.listarMaterias()
        if len(materia) > 0:
            funcionesMateria.listarMaterias(materia)
        else:
            print("No se encuentran materias")
        seleccion = funcionesSeleccionProf.pedirDatosRegistro()
        try:
            dao.registrarSeleccionProf(seleccion)
        except:
            print("Ocurrio un error.")
    elif opcion == 3:
        seleccion = dao.listarSeleccionProfs()
        if len(seleccion) > 0:
            sel = funcionesSeleccionProf.pedirDatosActualizacion(seleccion)
            if sel:
                dao.actualizarSeleccionProf(sel)
            else:
                print("ID de seleccion no encontrado.")
    elif opcion == 4:
        try:
            seleccion = dao.listarSeleccions()
            if len(seleccion) > 0:
                codigoEleminar = funcionesSeleccionProf.pedirDatosEliminacion(seleccion)
                if not(codigoEleminar == ""):
                    dao.eliminarSeleccionProf(codigoEleminar)
                else:
                    print("Codigo de seleccion no encontrado.")
            else:
                print("No se encontro seleccion.")
        except:
            print("Ocurrio un error.")

    else:
        print("Opcion no valida.")



    