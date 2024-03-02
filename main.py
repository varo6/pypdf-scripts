from src import PyMerger
def main():
    try:
        merger = PyMerger()
    except FileNotFoundError as e:
        print("Error:", e)

if __name__=="__main__":
    main()