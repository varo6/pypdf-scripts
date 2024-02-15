import os
from pypdf import PdfWriter

##Get current path as string, head to the pdfs folder
parent_path = os.path.dirname(os.path.abspath(__file__))
pdfs_path = os.path.join(parent_path,"pdfs")

##Get array of files located in the path
mylist = os.listdir(pdfs_path);

##Merge pdf files
merger = PdfWriter()

for pdf in mylist:
    if pdf.lower().endswith('.pdf'):
        currentFile = os.path.join(pdfs_path, pdf)
        print("Appending " +currentFile+ " to the merged pdf")
        merger.append(r""+currentFile)

currentFile = os.path.join(parent_path,"saved results","mergedpdf.pdf")
merger.write(currentFile)

##Check if mergedpdf was created and if it's not null
if currentFile is not None:
    print("Merge completed!")
merger.close()
