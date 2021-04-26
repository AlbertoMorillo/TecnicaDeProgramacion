def listarProfesores(profesor):
    print("\nProfesores: ")
    contador = 1
    for cur in profesor:
        datos="{0}. ID {1} | Nombre: {2}"
        print(datos.format(contador, cur[0],cur[1]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro(): 
    nombre = input("Ingresar nombre: ")

    profesor = (nombre)
    return profesor

def pedirDatosEliminacion(profesor):
    listarProfesores(profesor)
    existeCodigo = False
    codigoEleminar = input("Nombre de la carrera a eliminar: ")
    for cur in profesor:
        if cur[1] == codigoEleminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEleminar = ""

    return codigoEleminar

def pedirDatosActualizacion(profesor):
    listarProfesores(profesor)

    existeCodigo = False
    codigoEleminar = input("Nombre del profesor a editar: ")
    for cur in profesor:
        if cur[1] == codigoEleminar:
            existeCodigo = True
            break
    
    if existeCodigo:
        nombre = codigoEleminar
        nombreNuevo = input("Ingresar nuevo nombre: ")
        carr = (nombre, nombreNuevo)
    else:
        carr = None
    
    return carr
