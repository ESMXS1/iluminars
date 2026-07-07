import ConexionBD
from ConexionBD import ConexionBD

db = ConexionBD("localhost", "root", "", "escuela")

db.conectar()

db.cerrar()