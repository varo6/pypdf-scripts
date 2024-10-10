from pypdf import PdfReader, PdfWriter

def make_pdfreader(fname):
        reader = PdfReader(fname)
        return reader


def make_pdfwriter():
    writer = PdfWriter()
    return writer


def extract_pages(name: str, pages: list[int]):
    reader = make_pdfreader(name)
    writer = make_pdfwriter()
    for page_num in pages:  # Pages 10 to 20 (inclusive)
        page = reader.pages[page_num-1]
        writer.add_page(page)
    return writer

def extract_pdf(name: str, pages, output: str):
    print(f"Extracting {name} for pages {pages}")
    writer = extract_pages(name, pages)
    with open (f"{output}.pdf", "wb") as output_pdf:
        writer.write(output_pdf)

