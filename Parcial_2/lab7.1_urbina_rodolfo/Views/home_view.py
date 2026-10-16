import tkinter as tk
from tkinter import ttk, messagebox
from Models.products_model import Product


class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("600x450")

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{nombre_usuario}",
            font=("Helvetica", 12),
            justify="center"
        )
        lbl_mensaje.pack(pady=10)

        self.products_frame()
        self.load_products()

    def products_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        tree_scroll = tk.Scrollbar(frame)
        tree_scroll.pack(side="right", fill="y")

        self.table = ttk.Treeview(
            frame,
            columns=("ID Products", "Name", "Price", "Stock"),
            show="headings",
            yscrollcommand=tree_scroll.set
        )
        tree_scroll.config(command=self.table.yview)

        self.table.heading("ID Products", text="ID")
        self.table.heading("Name", text="Producto")
        self.table.heading("Price", text="Precio")
        self.table.heading("Stock", text="Stock")

        self.table.column("ID Products", width=50, anchor="center")
        self.table.column("Name", width=270)
        self.table.column("Price", width=100, anchor="e")
        self.table.column("Stock", width=80, anchor="center")

        self.table.pack(fill="both", expand=True)

    def load_products(self):
        for fila in self.table.get_children():
            self.table.delete(fila)

        try:
            productos = Product().get_products()
        except ConnectionError as e:
            messagebox.showerror("Error de conexión", str(e))
            return

        for p in productos:
            self.table.insert(
                "", tk.END,
                values=(p["id_product"], p["nombre"], f"${p['precio']:,.2f}", p["stock"])
            )