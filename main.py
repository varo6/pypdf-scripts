from src import PyMerger
try:
    merger = PyMerger()
except FileNotFoundError as e:
    print("Error:", e)