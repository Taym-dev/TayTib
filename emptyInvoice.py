from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def createPdf(outputPath):
	c = canvas.Canvas(outputPath, pagesize=A4)

	c.setFont("Helvetica", 12)
	
	offsetLeft = 50
	offsetRight = A4[0] - 225

	c.drawString(offsetRight, A4[1] - (100 + (18 * 0)), "TayTib")
	c.drawString(offsetRight, A4[1] - (100 + (18 * 1)), "Van Bosseplantsoen 6")
	c.drawString(offsetRight, A4[1] - (100 + (18 * 2)), "3317PH Dordrecht")

	c.drawString(offsetRight, A4[1] - (175 + (18 * 0)), "KVK:  896467")
	c.drawString(offsetRight, A4[1] - (175 + (18 * 1)), "BTW:  NL531532567B01")
	c.drawString(offsetRight, A4[1] - (175 + (18 * 2)), "Bank:  NL91ABNA0417164300")

	c.drawString(offsetLeft, A4[1] - (275 + (18 * 0)), "NAAM_VAN_KLANT")
	c.drawString(offsetLeft, A4[1] - (275 + (18 * 1)), "ADRES_VAN_KLANT")
	c.drawString(offsetLeft, A4[1] - (275 + (18 * 2)), "POSTCODE_STAD_VAN_KLANT")

	c.setFont("Helvetica", 24)
	c.drawString(offsetLeft, A4[1] - (375 + (28 * 0)), "FACTUUR")
	
	c.setFont("Helvetica", 12)
	c.drawString(offsetLeft, A4[1] - (395 + (18 * 0)), "Factuurnummer: N/A")

	c.drawString(offsetRight, A4[1] - (375 + (18 * 0)), "Factuurdatum: 01-01-1970")
	c.drawString(offsetRight, A4[1] - (375 + (18 * 1)), "Vervaldatum:   01-01-1970")

	c.drawString(100, A4[1] - (435 + (18 * 0)), "Omschrijving")
	c.drawString(325, A4[1] - (435 + (18 * 0)), "Bedrag")
	c.drawString(410, A4[1] - (435 + (18 * 0)), "Totaal")
	c.drawString(500, A4[1] - (435 + (18 * 0)), "BTW")

	c.line(50, 400, 535, 400)

	for i in range(3):
		c.drawString(55, A4[1] - (457 + (18 * i)), "1x")
		c.drawString(100, A4[1] - (457 + (18 * i)), "Artikel")
		c.drawString(325, A4[1] - (457 + (18 * i)), "€99.999,99")
		c.drawString(410, A4[1] - (457 + (18 * i)), "€99.999,99")
		c.drawString(500, A4[1] - (457 + (18 * i)), "21%")

		c.line(50, (400 - (20 * i)), 535, (400 - (20 * i)))

	c.save()

createPdf("invoice.pdf")