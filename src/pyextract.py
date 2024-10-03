import os
from pypdf import PdfReader, PdfWriter


def get_filename():
    fname = input("Enter the filename")
    if not fname:
        fname = "example.pdf"
    return fname

def get_npages():
    npages = input("Enter the number of pages (can be comma-separated or hyphenated): ")
    
    # Si el input está vacío, devuelve una lista con la página 1 como valor predeterminado
    if not npages:
        return [1]
    
    # Si el input contiene un guion, es un rango
    if '-' in npages:
        start, end = map(int, npages.split('-'))
        return list(range(start, end + 1))
    
    # Si el input contiene comas, es una lista de valores
    if ',' in npages:
        return list(map(int, npages.split(',')))
    
    # Si el input es un solo número
    return [int(npages)]

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
    print(os.getcwd())
    writer = extract_pages()
    with open ("result.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

print("Pages 10-20 have been extracted successfully!")
