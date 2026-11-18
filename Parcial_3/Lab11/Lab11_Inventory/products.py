"""
products.py
Responsabilidad única (SRP): la clase Producto conoce y protege SU PROPIO stock.
Valida que cada retiro sea correcto antes de modificar el estado.
"""

from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    """Representa un producto con código, nombre y stock disponible."""

    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def retirar(self, cantidad):
        """Retira 'cantidad' unidades del stock y regresa el stock restante.

        Todas las validaciones se hacen ANTES de modificar self.stock; si alguna
        falla se usa 'raise' para lanzar la excepción y el método termina en ese
        punto, por lo que el stock queda intacto.
        """
        # Validación 1: la cantidad debe ser un entero.
        # bool es subclase de int en Python (True == 1), así que se excluye
        # explícitamente para que retirar(True) no se acepte como "1 unidad".
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            # raise: interrumpe la ejecución y envía el error a quien llamó.
            raise CantidadInvalida(
                f"La cantidad debe ser un número entero (se recibió {cantidad!r})."
            )

        # Validación 2: la cantidad debe ser positiva (ni 0 ni negativa).
        if cantidad <= 0:
            raise CantidadInvalida(
                f"La cantidad debe ser mayor que 0 (se recibió {cantidad})."
            )

        # Validación 3: no se puede retirar más de lo que hay en stock.
        if cantidad > self.stock:
            raise StockInsuficiente(
                f"Stock insuficiente para '{self.nombre}': "
                f"se pidieron {cantidad} y solo hay {self.stock}."
            )

        # Solo si TODAS las validaciones pasaron se modifica el stock.
        self.stock -= cantidad
        return self.stock

    def __str__(self):
        return f"{self.codigo:<6} {self.nombre:<12} stock: {self.stock}"
