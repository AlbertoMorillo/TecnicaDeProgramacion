def listarPensums(pensum):
    print("\nPensums: ")
    contador = 1
    for cur in pensum:
        datos="{0}. ID {1} | ID Carrera: {2} | ID Materia: {3} )"
        print(datos.format(contador, cur[0],cur[2],cur[1]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro():
    idCarrera = input("Ingresar id de la carrera: ")
    idMateria = int(input("Ingresar id de la materia: "))

    pensum = (idCarrera, idMateria)
    return pensum

def pedirDatosEliminacion(pensum):
    listarPensums(pensum)
    existeCodigo = False
    codigoEleminar = int(input("Id del pensum a eliminar: "))
    for cur in pensum:
        if cur[0] == codigoEleminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEleminar = ""

    return codigoEleminar

def pedirDatosActualizacion(pensum):
    listarPensums(pensum)

    existeCodigo = False
    codigoEleminar = int(input("id del pensum a editar: "))
    for cur in pensum:
        if cur[0] == codigoEleminar:
            existeCodigo = True
            break
    
    if existeCodigo:
        codigo = codigoEleminar 
        codigoMat = input("Ingresar id de materia: ")
    
        pen = (codigo, codigoMat)
    else:
        pen = None
    
    return pen
