from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw 
        self.db = Database_connection()

    def auth(self):
        query = "SELECT * FROM users WHERE username = %s AND passw = %s" 
        
        result = self.db.ejecutar_consulta(query, (self.username, self.password))
        
        return result