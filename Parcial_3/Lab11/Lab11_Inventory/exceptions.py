"""
exceptions.py
Responsabilidad única (SRP): definir las excepciones personalizadas del sistema
de inventario. No contiene lógica de negocio ni de interfaz.
"""


class ErrorInventario(Exception):
    """Excepción base de todo el sistema de inventario.

    Todas las demás excepciones heredan de esta clase, de modo que un solo
    'except ErrorInventario' en main.py puede atrapar cualquiera de ellas
    gracias a la herencia (polimorfismo de excepciones).
    """
    pass


class ProductoNoEncontrado(ErrorInventario):
    """Se lanza cuando el código solicitado no existe en el inventario."""
    pass


class CantidadInvalida(ErrorInventario):
    """Se lanza cuando la cantidad no es un entero positivo (0, negativa o de otro tipo)."""
    pass


class StockInsuficiente(ErrorInventario):
    """Se lanza cuando se intenta retirar más unidades de las disponibles."""
    pass
