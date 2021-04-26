import mysql.connector
from mysql.connector import Error

class SeleccionDAO():
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
    
    def listarSeleccions(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM materiaestudiante ORDER BY idEstudiante DESC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarSeleccion(self, seleccion):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO materiaestudiante (idEstudiante, idMateria) VALUES ('{0}','{1}')"
                cursor.execute(sql.format(seleccion[0], seleccion[1]))
                self.conexion.commit()
                print("Seleccion registrado.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarSeleccion(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM materiaestudiante WHERE id = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Seleccion eliminado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarSeleccion(self, seleccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE materiaestudiante SET idMateria = '{0}' WHERE id = '{1}'"
                cursor.execute(sql.format(seleccion[1], seleccion[0]))
                self.conexion.commit()
                print("Seleccion actualizada.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))