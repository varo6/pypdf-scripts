from src import PyMerger
# Flet will be the interface package
import flet as ft 

# Will recieve page as a parameter. If not, create an ft.Page class
def main(page: ft.Page):

    # these two lines will align the text center in the app
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def button_clicked(e):
            try:
                # call src/PyMerger()
                merger = PyMerger()
                page.add(ft.Text(merger.to_string()))
            except FileNotFoundError as e:
                print("Error:", e)
        
    page.add(ft.ElevatedButton(text="Merge pdfs located on pdfs folder", on_click=button_clicked))


if __name__=="__main__":
    ft.app(target=main)