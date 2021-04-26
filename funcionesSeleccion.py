def listarSeleccions(seleccion):
    print("\nSelecciones: ")
    contador = 1
    for cur in seleccion:
        datos="{0}. ID {1} | ID Estudiante: {2} | ID Materia: {3} )"
        print(datos.format(contador, cur[0],cur[1],cur[2]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro():
    idMateria = int(input("Ingresar id de la materia: "))
    idEstudiante = int(input("Ingresar id del estudiante: "))

    seleccion = (idEstudiante,idMateria)
    return seleccion

def pedirDatosEliminacion(seleccion):
    listarSeleccions(seleccion)
    existeCodigo = False
    codigoEleminar = int(input("Id del seleccion a eliminar: "))
    for cur in seleccion:
        if cur[0] == codigoEleminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEleminar = ""

    return codigoEleminar

def pedirDatosActualizacion(seleccion):
    listarSeleccions(seleccion)

    existeCodigo = False
    codigoEleminar = int(input("id del seleccion a editar: "))
    for cur in seleccion:
        if cur[0] == codigoEleminar:
            existeCodigo = True
            break
    
    if existeCodigo:
        codigo = codigoEleminar 
        codigoMat = input("Ingresar id de materia: ")
    
        sel = (codigo, codigoMat)
    else:
        sel = None
    
    return sel
