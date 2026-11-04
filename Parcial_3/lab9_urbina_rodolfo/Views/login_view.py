import os
import tkinter as tk
from tkinter import messagebox
from Models.login_model import User
from Views.home_view import DashboardVentana


class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x380")
        self.root.resizable(False, False)
        self._aplicar_icono(self.root)

        self._crear_interfaz()

    def _aplicar_icono(self, ventana):
        """Pone assets/icono.png como ícono de la ventana (si el archivo existe)."""
        ruta_icono = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets", "icono.png"
        )
        try:
            ventana.icono = tk.PhotoImage(master=ventana, file=ruta_icono)
            ventana.iconphoto(True, ventana.icono)
        except tk.TclError:
            pass

    def _crear_interfaz(self):
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=25)

        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))

        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))

        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)
        self.entry_pass.bind("<Return>", lambda event: self._validar_login())

        btn_ingresar = tk.Button(
            self.root,
            text="Entrar",
            font=("Helvetica", 11, "bold"),
            bg="#095700",
            fg="black",
            cursor="hand2",
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=30)

        self.entry_usuario.focus()

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        try:
            usuario_obj = User(usuario_texto, pass_texto)
            datos_usuario = usuario_obj.auth()
        except ConnectionError as e:
            messagebox.showerror("Error de Conexión", str(e))
            return

        if datos_usuario and len(datos_usuario) > 0:
            usuario_encontrado = datos_usuario[0]
            nombre_usuario = usuario_encontrado.get('nombre', 'Usuario')

            messagebox.showinfo("Bienvenido", f"¡Hola {nombre_usuario}! Acceso concedido.")
            self._abrir_dashboard(nombre_usuario)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        self._aplicar_icono(root_dashboard)
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()