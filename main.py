from fpdf import FPDF
from fpdf.enums import XPos, YPos

def crear_pdf(nombre_archivo="documento.pdf"):
    """
    Crea un archivo PDF simple con un texto de ejemplo.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(200, 10, text="¡Hola, Mundo! Este es mi primer PDF con Python.", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.output(nombre_archivo)
    print(f"Se ha creado el archivo '{nombre_archivo}' exitosamente.")

if __name__ == "__main__":
    crear_pdf()