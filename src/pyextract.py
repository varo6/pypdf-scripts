from pypdf import PdfReader, PdfWriter
from .methods import get_filename, get_npages

def make_pdfreader(fname):
        reader = PdfReader(fname)
        return reader


def make_pdfwriter():
    writer = PdfWriter()
    return writer


def extract_pages():
    reader = make_pdfreader(get_filename())
    writer = make_pdfwriter()
    pages: list[int] = get_npages()
    for page_num in pages:  # Pages 10 to 20 (inclusive)
        page = reader.pages[page_num]
        writer.add_page(page)
    return writer

def extract_pdf():
    writer = extract_pages()
    with open ("result.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

print("Pages 10-20 have been extracted successfully!")
