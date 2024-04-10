from src import PyMerger
# Flet will be the interface package
import flet as ft
from flet import Row, Column
import os

# Will recieve page as a parameter. If not, create an ft.Page class


def main(page: ft.Page):

    page.bgcolor="#222831"
    page.window_width = 620        
    page.window_height = 380       
    page.window_resizable = False  
    page.update()
    # these two lines will align the text center in the app
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # FUNCTIONS SECION*************************************
    def pick_files_result(e: ft.FilePickerResultEvent):

        mylist = []
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)
                      ) if e.files else "Cancelled!"
        )

        for f in e.files:
            mylist.append(f.path)
        selected_files.update()
        print(mylist)
        print(selected_files)
        merger = PyMerger(mylist)

    def auto_clicked(e: ft.TapEvent):
        try:
            # call src/PyMerger()
            merger = PyMerger()
            page.add(ft.Text("auto clicked"))

        except FileNotFoundError as e:
            print("Error:", e)

    def manual_clicked(e: ft.TapEvent):
        try:
            print(e.control == b_auto)

            page.add(ft.Text("Manual clicked"))

        except FileNotFoundError as e:
            print("Error:", e)

    # Add both components to control files
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.add(selected_files)
    page.add(pick_files_dialog)

    # Buttons controlling the page
    b_manual = ft.ElevatedButton(
        text="ManualMerge", on_click=lambda _: pick_files_dialog.pick_files(initial_directory=True, allow_multiple=True), color="#BED7DC",  bgcolor="#31363F")
    b_auto = ft.ElevatedButton(
        text="AutoMerge", on_click=auto_clicked, color="#BED7DC",  bgcolor="#31363F")

    # Create a centered Row to hold the Columns for individual button centering
    centered_row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            # Create separate Columns for each button to center them horizontally
            Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[b_manual]
            ),
            Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[b_auto]
            )
        ]
    )

    page.add(centered_row)


if __name__ == "__main__":
    ft.app(target=main)
