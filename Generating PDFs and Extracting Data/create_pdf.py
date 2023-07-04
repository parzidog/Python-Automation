from fpdf import FPDF

# FPDF arguments: ORIENTATION - 'P' or 'L', UNIT - 'pt' is common, FORMAT - 'letter for US or 'A4' for EUR
pdf = FPDF(orientation="P", unit="pt", format="letter")
pdf.add_page()

# Use path to image, width and height. x and y coordinates are optional.
pdf.image("Resources/tiger.jpeg", w=80, h=50)

pdf.set_font(family="Times", style="B", size=24)

# .cell takes in the following arguments
# Width, 'w', in the specified unit where 0 is the full width
# Height, 'h', in the specified unit
# Text, 'txt', in the form of a string
# Align, 'align', with 'C', 'L' or 'R'
# Border, 'border', with a numeric value of 0 or 1 for the border or a string of 'L', 'R', 'T' or 'B'
pdf.cell(w=0, h=50, txt="Malayan Tiger", align="C", border="B", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=25, txt="Description", ln=1)

description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

pdf.multi_cell(w=0, h=15, txt=description, border="B")
pdf.set_font(family="Times", style="B", size=12)

pdf.ln()

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=75, h=25, txt="Kingdom:")


pdf.set_font(family="Times", size=12)
pdf.cell(w=75, h=25, txt="Animalia", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=75, h=25, txt="Phylum:")


pdf.set_font(family="Times", size=12)
pdf.cell(w=75, h=25, txt="Chordata")


pdf.output("Resources/create_pdf_output.pdf")
