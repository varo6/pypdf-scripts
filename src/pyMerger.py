import os
from pypdf import PdfWriter

class PyMerger:

    parent_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
    pdfs_path = os.path.join(parent_path, "pdfs")
    results_path = os.path.join(pdfs_path, "saved results")
    found_pdfs = False

    @staticmethod
    def merge(mylist):

        found_pdfs = PyMerger.found_pdfs
        # Merge pdf files
        merger = PdfWriter()
        counter = 0 
        results_path = PyMerger.results_path
        print("The object is " +str(mylist[0]))
        # Add all pdf files to the PdfWriter() Object
        for pdf in mylist:
            if pdf.lower().endswith('.pdf'):
                found_pdfs = True
                # currentFile = os.path.join(pdfs_path, pdf)
                currentFile = pdf
                print("Appending " + currentFile + " to the merged pdf")
                merger.append(r""+currentFile)

        if not found_pdfs:
            raise FileNotFoundError("Error: La carpeta de pdfs está vacía")

        # Check if mergedpdf exists and create the new pdf
        mylist = os.listdir(results_path)
        for pdf in mylist:
            if pdf.lower().startswith("mergedpdf"):
                counter = counter + 1
        if counter != 0:
            print("There are existing merged pdf files. Adding ID")
            currentFile = os.path.join(
                results_path, "mergedpdf" + str(counter)+".pdf")
            merger.write(currentFile)
        else:
            currentFile = os.path.join(results_path, "mergedpdf.pdf")
            merger.write(currentFile)

        # Check if mergedpdf was created and if it's not null
        if currentFile is not None:
            print ("Merge Completed!")
        merger.close()

    def to_string(self):
        return "Merge Completed!"
    

    def __init__(self, inputlist = None):

        if inputlist is not None:

            print("Manual merge chosen")
            PyMerger.merge(inputlist)
        else:
            # Get array of files located in the path
            mylist = os.listdir(PyMerger.pdfs_path)
            inputlist = list(map(lambda pdf: os.path.join(PyMerger.pdfs_path, pdf) , mylist ))
            print(str(inputlist))
            PyMerger.merge(inputlist)

