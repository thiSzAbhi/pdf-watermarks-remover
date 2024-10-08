from PyPDF2 import PdfWriter, PdfReader

def remove_watermark_in_batches(input_pdf, output_pdf, batch_size=100):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    num_pages = len(reader.pages)
    
    for i in range(0, num_pages, batch_size):
        end_page = min(i + batch_size, num_pages)
        print(f"Processing pages {i + 1} to {end_page}...")
        
        for j in range(i, end_page):
            page = reader.pages[j]
            # Remove watermark logic here
            # Add modified page to writer
            writer.add_page(page)
    
    # Write the processed output to a new PDF file
    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)

if __name__ == "__main__":
    input_pdf = "input_watermarked.pdf"
    output_pdf = "output_without_watermark.pdf"
    
    remove_watermark_in_batches(input_pdf, output_pdf)
