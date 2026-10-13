import mysql.connector
from mysql.connector import Error
from Controller.config import DB_CONFIG


class Database_connection:
    """Abre una conexión por consulta y ejecuta sentencias SQL con parámetros."""

    def ejecutar_consulta(self, query, params=None):
        conexion = None
        cursor = None
        try:
            conexion = mysql.connector.connect(**DB_CONFIG)
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(query, params)
            if cursor.description is not None:
                return cursor.fetchall()
            conexion.commit()
            return cursor.rowcount
        except Error as e:
            if conexion:
                conexion.rollback()
            raise ConnectionError(f"Error con la base de datos: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()