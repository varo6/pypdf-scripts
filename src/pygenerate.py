from fpdf import FPDF

def generate_pdf(text: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    lines = text.splitlines()
    for line in lines:
        pdf.cell(w=0,text= f"{line}", ln=True)

    pdf.output("holaa.pdf")
    print("hecho")
