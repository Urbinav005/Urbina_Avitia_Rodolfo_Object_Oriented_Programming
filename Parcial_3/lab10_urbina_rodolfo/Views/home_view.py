import os
import tkinter as tk
from tkinter import ttk, messagebox
from Controller.products_controller import ProductsController


class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal")
        self.root.geometry("600x500")
        self.controller = ProductsController()

        lbl_mensaje = tk.Label(
            self.root,
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{nombre_usuario}",
            font=("Helvetica", 12),
            justify="center"
        )
        lbl_mensaje.pack(pady=10)

        self.export_frame()
        self.products_frame()
        self.load_products()

    def export_frame(self):
        """Controles de exportación: menú de formato + botón."""
        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=20, pady=(0, 5))

        tk.Label(frame, text="Formato:", font=("Helvetica", 10)).pack(side="left")

        self.cmb_formato = ttk.Combobox(
            frame,
            values=["CSV", "TXT", "JSON", "PDF"],
            state="readonly",
            width=8
        )
        self.cmb_formato.current(0)
        self.cmb_formato.pack(side="left", padx=5)

        btn_exportar = ttk.Button(
            frame,
            text="Exportar Reporte",
            command=lambda: self.exportar_reporte(self.cmb_formato.get())
        )
        btn_exportar.pack(side="left", padx=5)

    def exportar_reporte(self, formato):
        try:
            ruta = self.controller.generar_reporte(formato)
        except (ConnectionError, ValueError, OSError) as e:
            messagebox.showerror("Error al exportar", str(e))
            return

        if messagebox.askyesno(
            "Reporte generado",
            f"Reporte {formato} guardado en:\n{ruta}\n\n¿Deseas abrirlo?"
        ):
            try:
                os.startfile(ruta)  # Windows
            except (AttributeError, OSError):
                messagebox.showinfo("Reporte generado", f"Abre el archivo en:\n{ruta}")

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
            productos = self.controller.obtener_productos()
        except ConnectionError as e:
            messagebox.showerror("Error de conexión", str(e))
            return

        for p in productos:
            self.table.insert(
                "", tk.END,
                values=(p["id_product"], p["nombre"], f"${p['precio']:,.2f}", p["stock"])
            )
