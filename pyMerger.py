import os
from pypdf import PdfWriter

##Get current path as string, head to the pdfs folder
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path,"pdfs")

##Get array of files located in the path
mylist = os.listdir(path);

##Merge pdf files
merger = PdfWriter()

for pdf in mylist:
    if pdf.lower().endswith('.pdf'):
        currentFile = os.path.join(path, pdf)
        print("Appending " +currentFile+ " to the merged pdf")
        merger.append(r""+currentFile)

merger.write(os.path.join(path,"mergedpdf.pdf"))

##Check if mergedpdf was created and if it's not null
currentFile = os.path.join(path, "mergedpdf.pdf")
if currentFile is not None:
    print("Merge completed!")
merger.close()
