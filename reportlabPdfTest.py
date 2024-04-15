from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def createPdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    c.setFont("Helvetica", 12)
    c.drawString(100, 750, text)

    c.save()

textContent = input("Voer een tekst in: ")

createPdf(textContent, "reportlab.pdf")