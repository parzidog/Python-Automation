import tabula

# Accepts two arguments:
#   Path to pdf
#   Number of page
table = tabula.read_pdf("Resources/weather.pdf", pages=1)

table[0].to_excel("Resources/pdf_to_excel.xlsx", index=None)
