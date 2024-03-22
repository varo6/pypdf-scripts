from src import PyMerger
# Flet will be the interface package
import flet as ft 
# Will recieve page as a parameter. If not, create an ft.Page class
def main(page: ft.Page):

    # these two lines will align the text center in the app
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def auto_clicked(e: ft.TapEvent):
            try:
                # call src/PyMerger()
                # merger = PyMerger(True)
                page.add(ft.Text("auto clicked"))
                


            except FileNotFoundError as e:
                print("Error:", e)

    def manual_clicked(e: ft.TapEvent):
            try:
                print(e.control == b_auto)
                # call src/PyMerger()
                # merger = PyMerger(True)
                page.add(ft.Text("Manual clicked"))


            except FileNotFoundError as e:
                print("Error:", e)
        
    b_auto = page.add(ft.ElevatedButton(text="AutoMerge", on_click=auto_clicked))
    b_manual = page.add(ft.ElevatedButton(text="ManualMerge", on_click=manual_clicked))

if __name__=="__main__":
    ft.app(target=main)