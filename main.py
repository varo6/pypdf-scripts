from src import PyMerger
#Flet will be the interface package
import flet as ft 

#Will recieve page as a parameter. If not, create an ft.Page class
def main(page: ft.Page):
    pass

    try:
        merger = PyMerger()   
    except FileNotFoundError as e:
        print("Error:", e)

if __name__=="__main__":
    ft.app(target=main)