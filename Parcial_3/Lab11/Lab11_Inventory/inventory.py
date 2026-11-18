"""
inventory.py
Responsabilidad única (SRP): la clase Inventario solo LOCALIZA productos por
código y delega el retiro al Producto correspondiente. No valida cantidades
(eso es trabajo de Producto) ni habla con el usuario (eso es trabajo de main.py).
"""

from exceptions import ProductoNoEncontrado
from products import Producto


class Inventario:
    """Colección de productos indexada por código."""

    def __init__(self):
        # Diccionario código -> Producto. Cada producto tiene código y stock distintos.
        self.productos = {
            "P001": Producto("P001", "Laptop", 10),
            "P002": Producto("P002", "Mouse", 25),
            "P003": Producto("P003", "Teclado", 15),
            "P004": Producto("P004", "Monitor", 5),
        }

    def retirar(self, codigo, cantidad):
        """Busca el producto por código y le pide que retire la cantidad.

        IMPORTANTE: aquí NO hay try/except. Si Producto.retirar() lanza
        CantidadInvalida o StockInsuficiente, la excepción se propaga
        automáticamente hacia main.py, que es quien decide cómo mostrarla.
        """
        # Validación: el código debe existir en el diccionario.
        if codigo not in self.productos:
            # raise: el inventario es responsable de reportar códigos inexistentes.
            raise ProductoNoEncontrado(f"No existe un producto con el código '{codigo}'.")

        # Delegación: Producto valida la cantidad y su propio stock.
        return self.productos[codigo].retirar(cantidad)

    def mostrar(self):
        """Regresa el inventario como texto (sin imprimir: la impresión es de main.py)."""
        return "\n".join(str(p) for p in self.productos.values())
