import pdfplumber
from PyPDF2 import PdfWriter, PdfReader

def remove_watermark_in_batches(input_pdf, output_pdf, batch_size=100):
    with pdfplumber.open(input_pdf) as pdf:
        writer = PdfWriter()
        total_pages = len(pdf.pages)
        
        # Process PDF in batches
        for start in range(0, total_pages, batch_size):
            end = min(start + batch_size, total_pages)
            print(f"Processing pages {start + 1} to {end}...")
            for page_num in range(start, end):
                page = pdf.pages[page_num]
                # Append page without watermark (assuming watermark removal logic)
                writer.add_page(page.to_pdf())  # Use your logic to modify the page

        # Write the processed pages to output PDF
        with open(output_pdf, "wb") as f_out:
            writer.write(f_out)

input_pdf = "input_watermarked.pdf"
output_pdf = "output_without_watermark.pdf"
remove_watermark_in_batches(input_pdf, output_pdf)
