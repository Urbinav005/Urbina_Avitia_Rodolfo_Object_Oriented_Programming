"""
main.py
Responsabilidad única (SRP): interactuar con el usuario. Lee la entrada,
llama al Inventario y muestra resultados o errores. No contiene reglas de negocio.
"""

from exceptions import ErrorInventario
from inventory import Inventario


def main():
    inventario = Inventario()

    while True:
        print("\n===== INVENTARIO =====")
        print(inventario.mostrar())

        codigo = input("\nCódigo del producto (o 'exit' para salir): ").strip().upper()
        if codigo == "EXIT":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        # try: agrupa las operaciones que pueden fallar.
        try:
            # int() lanza ValueError si el usuario escribe texto (ej. "abc").
            cantidad = int(input("Cantidad a retirar: "))
            # Puede lanzar ProductoNoEncontrado, CantidadInvalida o StockInsuficiente.
            restante = inventario.retirar(codigo, cantidad)

        # except ValueError: la entrada no se pudo convertir a número.
        except ValueError:
            print("Error [ValueError]: debes escribir un número entero, no texto.")

        # except ErrorInventario: atrapa TODAS sus subclases por herencia.
        # type(e).__name__ muestra cuál excepción específica ocurrió.
        except ErrorInventario as e:
            print(f"Error [{type(e).__name__}]: {e}")

        # else: solo se ejecuta si el bloque try terminó SIN excepciones.
        else:
            print(f"Retiro exitoso de {cantidad} unidad(es) del producto {codigo}. "
                  f"Stock restante: {restante}")


# Punto de entrada: main() solo se ejecuta si este archivo se corre directamente,
# no cuando se importa desde otro módulo.
if __name__ == "__main__":
    main()
