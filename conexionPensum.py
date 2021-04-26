import mysql.connector
from mysql.connector import Error

class PensumDAO():
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
    
    def listarPensums(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM materiacarrera ORDER BY idCarrera DESC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarPensum(self, pensum):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO materiacarrera (idCarrera, idMateria) VALUES ('{0}','{1}')"
                cursor.execute(sql.format(pensum[0], pensum[1]))
                self.conexion.commit()
                print("Pensum registrado.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarPensum(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM materiacarrera WHERE id = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Pensum eliminado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarPensum(self, pensum):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE materiacarrera SET idMateria = '{0}' WHERE id = '{1}'"
                cursor.execute(sql.format(pensum[1], pensum[0]))
                self.conexion.commit()
                print("Pensum actualizado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))