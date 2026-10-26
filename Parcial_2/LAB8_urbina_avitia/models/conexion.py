"""Modelo: clase encargada de abrir la conexión con MySQL."""
import mysql.connector


class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.usuario = "root"
        self.password = ""
        self.base_datos = "lab8_login"

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos
            )
            return conexion

        except mysql.connector.Error as error:
            print("Error al conectar con MySQL:", error)
            return None

    def probar_conexion(self):
        """Devuelve True si la conexión con MySQL funciona."""
        conexion = self.conectar()
        if conexion is not None and conexion.is_connected():
            print("Conexión exitosa a la base de datos:", self.base_datos)
            conexion.close()
            return True
        print("No fue posible conectar con la base de datos.")
        return False


if __name__ == "__main__":
    # Prueba rápida:  python -m models.conexion
    Conexion().probar_conexion()
