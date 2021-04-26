def listarEstudiantes(estudiante):
    print("\nEstudiantes: ")
    contador = 1
    for cur in estudiante:
        datos="{0}. ID {1} | Matricula: {2} | Nombre: {3} | Carrera ID: {4})"
        print(datos.format(contador, cur[0],cur[3],cur[1], cur[2]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro():
    codigo = int(input("Ingresar matricula: "))
    nombre = input("Ingresar nombre: ")
    carrera = int(input("Ingresar id carrera: "))

    estudiante = (codigo, nombre, carrera)
    return estudiante

def pedirDatosEliminacion(estudiante):
    listarEstudiantes(estudiante)
    existeCodigo = False
    codigoEleminar = int(input("Matricula del estudiante a eliminar: "))
    for cur in estudiante:
        if cur[3] == codigoEleminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEleminar = ""

    return codigoEleminar

def pedirDatosActualizacion(estudiante):
    listarEstudiantes(estudiante)

    existeCodigo = False
    codigoEleminar = int(input("Matricula del estudiante a editar: "))
    for cur in estudiante:
        if cur[3] == codigoEleminar:
            existeCodigo = True
            break
    
    if existeCodigo:
        codigo = codigoEleminar 
        nombre = input("Ingresar nombre: ")
    
        est = (codigo, nombre,)
    else:
        est = None
    
    return est
