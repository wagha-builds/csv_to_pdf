from fpdf import FPDF

#Orientation is either Portrait or Landscape.
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello World!", align="L", ln=1, border=1)
pdf.set_font(family="Times", style="B", size=10)
pdf.cell(w=0, h=10, txt="Hi World!", align="L", ln=1, border=1)

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello World!", align="L", ln=1)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, txt="Hi World!", align="L", ln=1)

pdf.output("output.pdf")
