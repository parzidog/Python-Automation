from fpdf import FPDF
import pandas

df = pandas.read_excel("Resources/data.xlsx")

for index, row in df.iterrows():
    pdf = FPDF(orientation="P", unit="pt", format="letter")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=50, txt=row["name"], border="B", ln=1)

    # Dynamically generate columns from rows
    for column in df.columns[1:]:
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=100, h=20, txt=column.capitalize())

        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=20, txt=row[column], ln=1)

    name = row["name"].lower().split(" ")
    name = "_".join(name)

    pdf.output(f"Resources/excel_{name}.pdf")
