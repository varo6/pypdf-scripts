import os
from pypdf import PdfWriter

##Get current path as string, head to the pdfs folder
parent_path = os.path.dirname(os.path.abspath(__file__))
pdfs_path = os.path.join(parent_path,"pdfs")
results_path = os.path.join(parent_path,"saved results")
counter = 0

##Get array of files located in the path
mylist = os.listdir(pdfs_path);

##Merge pdf files
merger = PdfWriter()

##Add all pdf files to the PdfWriter() Object
for pdf in mylist:
    if pdf.lower().endswith('.pdf'):
        currentFile = os.path.join(pdfs_path, pdf)
        print("Appending " +currentFile+ " to the merged pdf")
        merger.append(r""+currentFile)

##Check if mergedpdf exists and create the new pdf
mylist = os.listdir(results_path)
for pdf in mylist:
    if pdf.lower().startswith("mergedpdf"):
        counter = counter + 1
if counter != 0:
    print("There are existing merged pdf files. Adding ID")
    currentFile = os.path.join(results_path,"mergedpdf" + str(counter)+".pdf")
    merger.write(currentFile)  
else:
    currentFile = os.path.join(results_path,"mergedpdf.pdf")
    merger.write(currentFile)

##Check if mergedpdf was created and if it's not null
if currentFile is not None:
    print("Merge completed!")
merger.close()
