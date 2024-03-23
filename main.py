from src import PyMerger
# Flet will be the interface package
import flet as ft
# Will recieve page as a parameter. If not, create an ft.Page class


def main(page: ft.Page):

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
    b_manual = page.add(ft.ElevatedButton(
        text="ManualMerge", on_click=lambda _: pick_files_dialog.pick_files(initial_directory=True,allow_multiple=True)))
    b_auto = page.add(ft.ElevatedButton(
        text="AutoMerge", on_click=auto_clicked))



if __name__ == "__main__":
    ft.app(target=main)