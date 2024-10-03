import pytesseract
from .methods import get_filename, get_npages
from pdf2image import convert_from_path

def scan_pdf() -> str:
    name = get_filename()
    pages = get_npages()
    if pages is None:
        imgpages = convert_from_path(name, 600)
    else:
        imgpages = convert_from_path(name, 600, first_page=pages[0], last_page=pages[-1])
    text_data = ''
    print("Scanning...")
    for page in imgpages:
        text = pytesseract.image_to_string(page)
        text_data += text + '\n'
    return text_data
    
def scan_to_text():
    text = scan_pdf()
    with open('output.txt', 'w') as file:
        file.write(text)
    print("Text extracted and saved to output.txt")
