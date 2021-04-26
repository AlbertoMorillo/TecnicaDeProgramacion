import mysql.connector
from mysql.connector import Error

class SeleccionProfDAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host= 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'universidad'
            )
        except Error as ex:
            print("Error al internar la conexion {0}".format(e))
    
    def listarSeleccionProfs(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM materiaprofesor ORDER BY idProfesor DESC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarSeleccionProf(self, seleccion):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO materiaprofesor (idMateria,idProfesor) VALUES ('{0}','{1}')"
                cursor.execute(sql.format(seleccion[0], seleccion[1]))
                self.conexion.commit()
                print("Seleccion registrado.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarSeleccionProf(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM materiaprofesor WHERE id = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Seleccion eliminada.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarSeleccionProf(self, seleccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE materiaprofesor SET idMateria = '{0}' WHERE id = '{1}'"
                cursor.execute(sql.format(seleccion[1], seleccion[0]))
                self.conexion.commit()
                print("Seleccion actualizada.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))