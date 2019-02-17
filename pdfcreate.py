# simple_demo.py
 
from fpdf import FPDF
 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Courier", 'B',size=18)
pdf.cell(200, 10, txt="Preliminary Environmental Impact Statement", ln=1, align="L")
pdf.set_font("Courier", size=12)
pdf.multi_cell( 180, 5, "This preliminary environmental impact statement was prepared as a first look into the potential effects of a proposed construction plan on existing wildlife and infrastructure existent in the given geographical area. In compliance with the National Environmental Policy Act (NEPA) and other relevant Federal and State laws and regulations, an environmental impact statement is vital for any construction, renovation, or significant land alteration project. The environmental impact statement discloses the direct, indirect, and cumulative environmental impacts that would result from the proposed action and alternatives. The document is organized into four chapters: land use, existing wildlife, existing infrastructure, and construction impacts.", 0)

pdf.cell(200, 30, txt="Property being assessed:", ln=1, align="L")
pdf.output("simple_demo.pdf")


