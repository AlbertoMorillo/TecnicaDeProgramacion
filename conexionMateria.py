import mysql.connector
from mysql.connector import Error

class MateriaDAO():
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
    
    def listarMaterias(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM materia ORDER BY Nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))

    
    def registrarMateria(self, materia):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO materia (Codigo, Nombre, Credito) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(materia[0], materia[1], materia[2]))
                self.conexion.commit()
                print("Materia registrada.\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            

    def eliminarMateria(self, codigoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM materia WHERE Codigo = '{0}'"
                cursor.execute(sql.format(codigoEliminar))
                self.conexion.commit()
                print("Curso eliminado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))

    def actualizarMateria(self, materia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE materia SET Nombre = '{0}', Credito = '{1}' WHERE Codigo = '{2}'"
                cursor.execute(sql.format(materia[1], materia[2], materia[0]))
                self.conexion.commit()
                print("Curso actualizado.\n")
            except Error as ex:
                print("Error al intentar conectar {0}.".format(ex))