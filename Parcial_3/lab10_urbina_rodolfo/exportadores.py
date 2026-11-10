import csv
import json
from decimal import Decimal

from fpdf import FPDF


class Exportador:
    """Clase base (simula una interfaz). Cada formato debe sobrescribir exportar()."""

    extension = ""

    def exportar(self, datos, ruta_archivo):
        """Método que debe ser sobrescrito por las clases hijas"""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class ExportadorCSV(Exportador):
    extension = ".csv"

    def exportar(self, datos, ruta_archivo):
        # utf-8-sig para que Excel muestre bien los acentos
        with open(ruta_archivo, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Precio", "Stock"])
            for producto in datos:
                writer.writerow([
                    producto["id_product"],
                    producto["nombre"],
                    f"{producto['precio']:.2f}",
                    producto["stock"],
                ])
        print(f"Archivo CSV generado en: {ruta_archivo}")


class ExportadorTXT(Exportador):
    extension = ".txt"

    def exportar(self, datos, ruta_archivo):
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in datos:
                file.write(
                    f"ID: {producto['id_product']} | Nombre: {producto['nombre']} | "
                    f"Precio: ${producto['precio']:,.2f} | Stock: {producto['stock']}\n"
                )
            file.write(f"--- Total de productos: {len(datos)} ---\n")
        print(f"Archivo TXT generado en: {ruta_archivo}")


class ExportadorJSON(Exportador):
    extension = ".json"

    def exportar(self, datos, ruta_archivo):
        # MySQL regresa DECIMAL como Decimal, que json no sabe serializar
        registros = [
            {
                "id_product": p["id_product"],
                "nombre": p["nombre"],
                "precio": float(p["precio"]) if isinstance(p["precio"], Decimal) else p["precio"],
                "stock": p["stock"],
            }
            for p in datos
        ]
        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(registros, file, ensure_ascii=False, indent=4)
        print(f"Archivo JSON generado en: {ruta_archivo}")


class ExportadorPDF(Exportador):
    extension = ".pdf"

    @staticmethod
    def _texto(valor):
        # Las fuentes base de FPDF solo soportan latin-1 (acentos y ñ sí funcionan)
        return str(valor).encode("latin-1", "replace").decode("latin-1")

    def exportar(self, datos, ruta_archivo):
        pdf = FPDF()
        pdf.add_page()

        # Título
        pdf.set_font("Arial", "B", 16)
        pdf.cell(190, 10, self._texto("Reporte de Inventario de Productos"), 0, 1, "C")
        pdf.ln(5)

        # Encabezados de la tabla
        anchos = [20, 100, 40, 30]
        encabezados = ["ID", "Producto", "Precio", "Stock"]
        pdf.set_font("Arial", "B", 12)
        for ancho, titulo in zip(anchos, encabezados):
            pdf.cell(ancho, 10, titulo, 1, 0, "C")
        pdf.ln()

        # Cuerpo
        pdf.set_font("Arial", size=12)
        for producto in datos:
            pdf.cell(anchos[0], 10, self._texto(producto["id_product"]), 1, 0, "C")
            pdf.cell(anchos[1], 10, self._texto(producto["nombre"]), 1, 0, "L")
            pdf.cell(anchos[2], 10, self._texto(f"${producto['precio']:,.2f}"), 1, 0, "R")
            pdf.cell(anchos[3], 10, self._texto(producto["stock"]), 1, 0, "C")
            pdf.ln()

        pdf.ln(5)
        pdf.set_font("Arial", "I", 10)
        pdf.cell(190, 10, self._texto(f"Total de productos: {len(datos)}"), 0, 1, "R")

        pdf.output(ruta_archivo)
        print(f"Archivo PDF generado en: {ruta_archivo}")
