from Controller.database_connection import Database_connection

class Product:
    def __init__(self, nombre=None, precio=None, stock=None, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.db = Database_connection()

    def get_products(self):
        query = "SELECT * FROM products"
        return self.db.ejecutar_consulta(query)