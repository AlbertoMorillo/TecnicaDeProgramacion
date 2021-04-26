import mysql.connector
from mysql.connector import Error

class ProfesorDAO():
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
    
    def listarProfesors(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM profesor ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarProfesor(self, profesor):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO profesor (nombre) VALUES ('{0}')"
                cursor.execute(sql.format(profesor))
                self.conexion.commit()
                print("Profesor registrada.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarProfesor(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM profesor WHERE nombre = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Profesor eliminado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarProfesor(self, profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE profesor SET nombre = '{0}' WHERE nombre = '{1}'"
                cursor.execute(sql.format(profesor[1], profesor[0]))
                self.conexion.commit()
                print("Profesor actualizado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))