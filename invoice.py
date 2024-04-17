from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def createInvoice(invoiceInfo, clientInfo, products, outputPath):
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

	c.drawString(offsetLeft, A4[1] - (275 + (18 * 0)), clientInfo['name'])
	c.drawString(offsetLeft, A4[1] - (275 + (18 * 1)), clientInfo['address'])
	c.drawString(offsetLeft, A4[1] - (275 + (18 * 2)), clientInfo['postalCity'])

	c.setFont("Helvetica", 24)
	c.drawString(offsetLeft, A4[1] - (375 + (28 * 0)), "FACTUUR")
	
	c.setFont("Helvetica", 12)
	c.drawString(offsetLeft, A4[1] - (395 + (18 * 0)), f"Factuurnummer: {invoiceInfo['id']}")

	c.drawString(offsetRight, A4[1] - (375 + (18 * 0)), f"Factuurdatum: {invoiceInfo['createdAt']}")
	c.drawString(offsetRight, A4[1] - (375 + (18 * 1)), f"Vervaldatum:   {invoiceInfo['expiresAt']}")

	c.drawString(100, A4[1] - (435 + (18 * 0)), "Omschrijving")
	c.drawString(325, A4[1] - (435 + (18 * 0)), "Bedrag")
	c.drawString(410, A4[1] - (435 + (18 * 0)), "Totaal")
	c.drawString(500, A4[1] - (435 + (18 * 0)), "BTW")

	c.line(50, 400, 535, 400)

	subTotal = 0
	totalTax = 0

	for i, product in enumerate(products):
		productTotal = product['prijs_per_stuk_excl_btw'] * product['aantal']

		subTotal += productTotal
		totalTax += productTotal * (product['btw_percentage'] / 100)

		c.drawString(55, A4[1] - (456 + (21 * i)), f"{product['aantal']}x")
		c.drawString(100, A4[1] - (456 + (21 * i)), f"{product['productnaam']}")
		c.drawString(325, A4[1] - (456 + (21 * i)), f"€{product['prijs_per_stuk_excl_btw']}")
		c.drawString(410, A4[1] - (456 + (21 * i)), f"€{productTotal}")
		c.drawString(500, A4[1] - (456 + (21 * i)), f"{product['btw_percentage']}%")

		c.line(50, (379 - (21 * i)), 535, (379 - (21 * i)))
	
	c.drawString(325, A4[1] - (458 + (21 * (i + 1))), "Subtotaal")
	c.drawString(410, A4[1] - (458 + (21 * (i + 1))), f"€{subTotal}")

	c.drawString(325, A4[1] - (457 + (21 * (i + 2))), "BTW")
	c.drawString(410, A4[1] - (457 + (21 * (i + 2))), f"€{totalTax}")

	c.line(310, (334 - (21 * i)), 490, (334 - (21 * i)))

	c.drawString(325, A4[1] - (461 + (21 * (i + 3))), "Totaal")
	c.drawString(410, A4[1] - (461 + (21 * (i + 3))), f"€{round(subTotal + totalTax, 2)}")

	c.setFont("Helvetica", 10)
	c.drawString(50, 66, f"Wij verzoek u om de betaling binnen {invoiceInfo['term']} te voldoen op rekening NL91ABNA0417164300")
	c.drawString(50, 50, "onder vermelding van het factuurnummer.")

	c.save()

# Test
INVOICE_INFO = {
	"id": "69420",
	"createdAt": "20-04-2024",
	"expiresAt": "24-04-2024",
	"term": "60-dagen"
}

CLIENT_INFO = {
	"name": "Chaturbate",
	"address": "Vishaven 243",
	"postalCity": "6969PH Taymstad"
}

PRODUCTS = [
	{ "productnaam": "Dildo", "aantal": 5, "prijs_per_stuk_excl_btw": 30, "btw_percentage": 21 },
	{ "productnaam": "Dildo XXL", "aantal": 2, "prijs_per_stuk_excl_btw": 30, "btw_percentage": 9 }
]

createInvoice(INVOICE_INFO, CLIENT_INFO, PRODUCTS, "invoice.pdf")