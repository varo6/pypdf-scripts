import pytesseract
from pdf2image import convert_from_path
from .pygenerate import generate_pdf

def scan_pdf(name: str, pages) -> str:
    if pages is None:
        imgpages = convert_from_path(name, 600)
    else:
        imgpages = convert_from_path(
            name, 600, first_page=(pages[0]), last_page=(pages[-1]),
        )
    text_data = ""
    print("Scanning...")
    iter = 1
    for page in imgpages:
        text = pytesseract.image_to_string(page)
        text_data += text + "\n"
        iter +=1
    return text_data


def scan_to_text(filename: str, pages, output: str):

    if pages.length > 10:
        for i in range(0, len(pages), 10):
            write_pdf( scan_pdf(filename, pages[i:i+10]), output)

def write_pdf(text: str, output: str):

    print(f"writing to {output}.txt")
    with open(f"{output}.txt", "w") as file:
        file.write(text)
#    generate_pdf(text)
#    print(f"Text extracted and saved to {output}.txt")
