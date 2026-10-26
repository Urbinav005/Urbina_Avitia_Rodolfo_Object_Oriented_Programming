"""Vista: ventana secundaria para registrar usuarios."""
import tkinter as tk
from tkinter import messagebox


class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        # PERSONALIZAR 1:
        # Cambia el título de la ventana.
        self.ventana.title("LAB 8 - Nuevo usuario")

        # PERSONALIZAR 2:
        # Modifica las dimensiones de la ventana.
        self.ventana.geometry("460x480")

        # PERSONALIZAR 3:
        # Cambia el color de fondo.
        self.ventana.configure(bg="#212F3D")

        self.ventana.resizable(False, False)

        # Mantiene la ventana asociada a la principal.
        self.ventana.transient(root)
        self.ventana.grab_set()

        # PERSONALIZAR 4:
        # Cambia el título, la fuente y sus colores.
        self.titulo = tk.Label(
            self.ventana,
            text="REGISTRO",
            font=("Segoe UI", 20, "bold"),
            bg="#212F3D",
            fg="#58D68D"
        )
        self.titulo.pack(pady=18)

        # PERSONALIZAR 5:
        # Modifica el texto y estilo de las etiquetas.
        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#212F3D",
            fg="#ECF0F1",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=35,
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg="#212F3D",
            fg="#ECF0F1",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=35,
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg="#212F3D",
            fg="#ECF0F1",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#212F3D",
            fg="#ECF0F1",
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.entry_confirmar.pack(pady=4)

        # PERSONALIZAR 6:
        # Cambia el texto, color, fuente y tamaño del botón.
        self.btn_guardar = tk.Button(
            self.ventana,
            text="Guardar registro",
            width=24,
            bg="#58D68D",
            fg="#212F3D",
            activebackground="#82E0AA",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        # Botón para cancelar el registro.
        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=22,
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()
