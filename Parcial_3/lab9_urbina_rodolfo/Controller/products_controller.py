import os
from datetime import datetime

from Models.products_model import Product
from exportadores import ExportadorCSV, ExportadorTXT, ExportadorJSON, ExportadorPDF


class ProductsController:
    """Intermediario entre la Vista (home_view) y el Modelo (Product)."""

    # Cada formato apunta a su clase hija; así no hay una cadena de if/elif
    EXPORTADORES = {
        "CSV": ExportadorCSV,
        "TXT": ExportadorTXT,
        "JSON": ExportadorJSON,
        "PDF": ExportadorPDF,
    }

    CARPETA_REPORTES = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Reportes"
    )

    def __init__(self):
        self.modelo = Product()

    def obtener_productos(self):
        return self.modelo.get_products()

    def generar_reporte(self, formato):
        """Exporta todos los productos al formato elegido y regresa la ruta del archivo."""
        clase_exportador = self.EXPORTADORES.get(formato)
        if clase_exportador is None:
            raise ValueError(f"Formato no soportado: {formato}")

        # 1. Pedir los datos al Modelo
        datos = self.modelo.get_products()

        # 2. Instanciar solo la clase hija correspondiente
        exportador = clase_exportador()

        os.makedirs(self.CARPETA_REPORTES, exist_ok=True)
        marca = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.join(
            self.CARPETA_REPORTES, f"reporte_productos_{marca}{exportador.extension}"
        )

        # 3. Polimorfismo: al Controlador no le importa qué formato es
        exportador.exportar(datos, ruta)
        return ruta
