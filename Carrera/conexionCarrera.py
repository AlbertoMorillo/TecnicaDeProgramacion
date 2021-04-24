import mysql.connector
from mysql.connector import Error

class CarreraDAO():
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
    
    def listarCarreras(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM carrera ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarCarrera(self, carrera):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO carrera (nombre) VALUES ('{0}')"
                cursor.execute(sql.format(carrera))
                self.conexion.commit()
                print("Carrera registrada.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarCarrera(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM carrera WHERE nombre = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Curso eliminado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarCarrera(self, carrera):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE carrera SET nombre = '{0}' WHERE nombre = '{1}'"
                cursor.execute(sql.format(carrera[1], carrera[0]))
                self.conexion.commit()
                print("Curso actualizado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))