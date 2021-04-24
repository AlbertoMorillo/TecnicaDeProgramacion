def listarMaterias(materia):
    print("\nMaterias: ")
    contador = 1
    for cur in materia:
        datos="{0}. ID {1} | Codigo: {2} (Nombre: {3}. Creditos {4})"
        print(datos.format(contador, cur[0],cur[1],cur[2], cur[3]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro():
    codigo = input("Ingresar codigo: ")  
    nombre = input("Ingresar nombre: ")
    credito = int(input("Ingresar credito: "))

    materia = (codigo, nombre, credito)
    return materia

def pedirDatosEliminacion(materia):
    listarMaterias(materia)
    existeCodigo = False
    codigoEleminar = input("Codigo del curso a eliminar.")
    for cur in materia:
        if cur[1] == codigoEleminar:
            existeCodigo = True
            break
    
    if not existeCodigo:
        codigoEleminar = ""

    return codigoEleminar

def pedirDatosActualizacion(materia):
    listarMaterias(materia)

    existeCodigo = False
    codigoEleminar = input("Codigo del curso a editar.")
    for cur in materia:
        if cur[1] == codigoEleminar:
            existeCodigo = True
            break
    
    if existeCodigo:
        codigo = input("Ingresar codigo: ")  
        nombre = input("Ingresar nombre: ")
        credito = int(input("Ingresar credito: "))
    
        curso = (codigo, nombre, credito)
    else:
        curso = None
    
    return curso
