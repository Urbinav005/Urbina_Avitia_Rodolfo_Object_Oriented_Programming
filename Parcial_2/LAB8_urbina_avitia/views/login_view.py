"""Vista: ventana principal de inicio de sesión."""
import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root):
        self.root = root

        # PERSONALIZAR 1:
        # Cambia el título de la ventana.
        self.root.title("LAB 8 - Acceso | Rodolfo Urbina Avitia")

        # PERSONALIZAR 2:
        # Modifica el ancho y alto de la ventana.
        self.root.geometry("460x400")

        # PERSONALIZAR 3:
        # Cambia el color de fondo.
        self.root.configure(bg="#1B2631")

        self.root.resizable(False, False)

        # PERSONALIZAR 4:
        # Cambia el texto, la fuente y los colores del título.
        self.titulo = tk.Label(
            root,
            text="BIENVENIDO",
            font=("Segoe UI", 22, "bold"),
            bg="#1B2631",
            fg="#F4D03F"
        )
        self.titulo.pack(pady=20)

        # PERSONALIZAR 5:
        # Modifica el texto y la apariencia de las etiquetas.
        self.lbl_email = tk.Label(
            root,
            text="Correo:",
            font=("Segoe UI", 11, "bold"),
            bg="#1B2631",
            fg="#ECF0F1"
        )
        self.lbl_email.pack()

        # PERSONALIZAR 6:
        # Cambia el ancho, la fuente y otros atributos del campo.
        self.entry_email = tk.Entry(
            root,
            width=32,
            font=("Segoe UI", 12),
            bg="#FDFEFE",
            relief="flat",
            justify="center"
        )
        self.entry_email.pack(pady=5, ipady=4)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña:",
            font=("Segoe UI", 11, "bold"),
            bg="#1B2631",
            fg="#ECF0F1"
        )
        self.lbl_password.pack()

        # El atributo show oculta los caracteres al escribir.
        self.entry_password = tk.Entry(
            root,
            width=32,
            font=("Segoe UI", 12),
            bg="#FDFEFE",
            relief="flat",
            justify="center",
            show="•"
        )
        self.entry_password.pack(pady=5, ipady=4)

        # PERSONALIZAR 7:
        # Cambia el texto, color, tamaño y fuente del botón.
        self.btn_login = tk.Button(
            root,
            text="Entrar",
            width=22,
            bg="#F4D03F",
            fg="#1B2631",
            activebackground="#F7DC6F",
            font=("Segoe UI", 12, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        # PERSONALIZAR 8:
        # Cambia el diseño del botón para abrir el registro.
        self.btn_register = tk.Button(
            root,
            text="¿No tienes cuenta? Regístrate",
            width=28,
            bg="#1B2631",
            fg="#5DADE2",
            activebackground="#1B2631",
            font=("Segoe UI", 10, "underline"),
            relief="flat",
            bd=0,
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)
