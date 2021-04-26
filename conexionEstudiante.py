import mysql.connector
from mysql.connector import Error

class EstudianteDAO():
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
    
    def listarEstudiantes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM estudiante ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarEstudiante(self, estudiante):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO estudiante (matricula, nombre, carrera) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(estudiante[0], estudiante[1], estudiante[2]))
                self.conexion.commit()
                print("Estudiante registrada.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarEstudiante(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM estudiante WHERE matricula = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Estudiante eliminado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarEstudiante(self, estudiante):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE estudiante SET nombre = '{0}' WHERE matricula = '{1}'"
                cursor.execute(sql.format(estudiante[1], estudiante[0]))
                self.conexion.commit()
                print("Estudiante actualizado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))