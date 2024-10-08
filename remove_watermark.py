import pdfplumber
from fpdf import FPDF

def remove_watermark_with_pdfplumber(input_pdf, output_pdf):
    with pdfplumber.open(input_pdf) as pdf:
        fpdf = FPDF()

        for page in pdf.pages:
            text = page.extract_text()

            # Create a new PDF page
            fpdf.add_page()
            fpdf.set_auto_page_break(auto=True, margin=15)
            fpdf.set_font("Arial", size=12)
            fpdf.multi_cell(0, 10, text)

        fpdf.output(output_pdf)

input_pdf = "input_watermarked.pdf"
output_pdf = "output_without_watermark_plumber.pdf"
remove_watermark_with_pdfplumber(input_pdf, output_pdf)
