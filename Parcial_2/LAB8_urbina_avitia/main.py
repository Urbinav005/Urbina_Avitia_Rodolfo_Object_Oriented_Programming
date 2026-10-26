"""Punto de entrada de la aplicación (arquitectura MVC)."""
import tkinter as tk

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.auth_controller import Authentication


class System:

    def __init__(self):
        self.root = tk.Tk()

        # Modelo, vista y controlador.
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.start()
