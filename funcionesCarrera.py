def listarCarerras(carerra):
    print("\nCarerras: ")
    contador = 1
    for cur in carerra:
        datos="{0}. ID {1} | Nombre: {2}"
        print(datos.format(contador, cur[0],cur[1]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro(): 
    nombre = input("Ingresar nombre: ")

    carerra = (nombre)
    return carerra

def pedirDatosEliminacion(carerra):
    listarCarerras(carerra)
    existeCodigo = False
    codigoEleminar = input("Nombre de la carrera a eliminar: ")
    for cur in carerra:
        if cur[1] == codigoEleminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEleminar = ""

    return codigoEleminar

def pedirDatosActualizacion(carerra):
    listarCarerras(carerra)

    existeCodigo = False
    codigoEleminar = input("Nombre de la materia a editar: ")
    for cur in carerra:
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
