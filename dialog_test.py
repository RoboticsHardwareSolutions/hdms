import flet
from flet import (
    AlertDialog,
    border,
    DataCell,
    DataTable,
    ListView,
    AppBar,
    Column,
    MainAxisAlignment,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    TemplateRoute,
    Text,
    TextField,
    DataColumn,
    DataRow,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
)
from pymongo import MongoClient


def main(page):
    print("start")

    def button_add_clicked(e):
        page.update()
        print("updated")

    def create_new_product():
        print("new product created")

    def open_dialog(e):
        dialogs = Column(
            [
                TextField(label="Name"),  # TODO on_change=textfield_change on_submit=
                # TextField(label="Type"),  # TODO on_change=textfield_change on_submit=
                # TextField(label="Description"),  # TODO on_change=textfield_change on_submit=
                # TextField(label="Comment"),
            ],
            alignment="spaceBetween",
        )

        dialog = AlertDialog(
            title=Text("New product"),
            actions=[
                dialogs,

            ],
            actions_alignment=MainAxisAlignment.CENTER,
            # clip_behavior="hardEdge",
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    page.add(ElevatedButton(text="ADD", on_click=button_add_clicked, data=0))
    page.add(ElevatedButton(text="Create", on_click=open_dialog))


# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
flet.app(target=main)
