import os
from src import PyMerger
from src import pyextract
def pick_files():
    # Aquí podrías implementar una forma de seleccionar archivos sin GUI
    # Por ejemplo, podrías pedir al usuario que introduzca las rutas de los archivos
    paths = input("Introduce las rutas de los archivos separadas por comas: ").split(',')
    return [path.strip() for path in paths]

def auto_merge():
    try:
        merger = PyMerger()
        print("Auto merge iniciado")
        # Aquí irían las operaciones de auto merge
    except FileNotFoundError as e:
        print("Error:", e)

def manual_merge():
    try:
        files = pick_files()
        if files:
            merger = PyMerger(files)
            print("Merge manual iniciado con los archivos:", files)
            # Aquí irían las operaciones de merge manual
        else:
            print("No se seleccionaron archivos")
    except FileNotFoundError as e:
        print("Error:", e)

def main():
    while True:
        print("\n1. Merge Manual")
        print("2. Auto Merge")
        print("3. Exportar páginas")
        print("4. Salir")
        choice = input("Elige una opción (1-4): ")

        if choice == '1':
            manual_merge()
        elif choice == '2':
            auto_merge()
        elif choice == '3':
            pyextract.extract_pdf()
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
