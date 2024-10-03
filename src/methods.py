def get_filename():
    fname = input("Enter the filename")
    if not fname:
        fname = "example.pdf"
    return fname

def get_npages():
    npages = input("Enter the number of pages (can be comma-separated or hyphenated): ")
    
    # Si el input está vacío, devuelve una lista con la página 1 como valor predeterminado
    if not npages:
        return None
    
    # Si el input contiene un guion, es un rango
    if '-' in npages:
        start, end = map(int, npages.split('-'))
        return list(range(start, end + 1))
    
    # Si el input contiene comas, es una lista de valores
    if ',' in npages:
        return list(map(int, npages.split(',')))
    
    # Si el input es un solo número
    return [int(npages)]



