import mysql.connector
from mysql.connector import Error

class ConexionBD:
    """Administra la conexión a un servidor MySQL."""

    def __init__(self, host, usuario, contrasena, bd):
        self.datos = dict(
            host=host,
            user=usuario,
            password=contrasena,
            database=bd
        )

        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.datos)
            print("Conexion exitosa a", self.datos["database"])
        except Error as err:
            print("Error al conectar:", err)

    def cerrar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexion cerrada.")