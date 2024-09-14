import flet
import pymongo
import prob_db as db
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
    ScrollMode,
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
    SafeArea,
    DataRow,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
)
from flet_core import ClipBehavior
from pymongo import MongoClient


def main(page):
    name_field = TextField(label="Name")
    description_filed = TextField(label="Description")
    comments_field = TextField(label="Comment")
    text_msg = Column([Text(value="Enter all fields and tap create")],
                      alignment=MainAxisAlignment.CENTER)
    prod = db.ProdDB("localhost", 27017)

    def add_new_dialog(e):
        enter_fields = Column(
            [
                name_field,
                description_filed,
                comments_field,
            ],
            alignment=MainAxisAlignment.CENTER,
        )
        buttons = Row(
            [
                ElevatedButton(text="Cancel", on_click=create_new_product),
                ElevatedButton(text="Create", on_click=create_new_product),
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,

        )
        dialog = AlertDialog(
            title=Text("New product"),
            content=Column(
                [
                    enter_fields,
                    text_msg,
                    buttons,
                ]
            ),
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def create_new_product(e):
        if ((hasattr(e.control, "text") and not e.control.text == "Cancel") or
                (type(e.control) is TextField and e.control.value != "")):
            res = prod.add(name_field.value, description_filed.value, comments_field.value)
            text_msg.controls[0].value = res
            if res != "Added!":
                text_msg.controls[0].color = flet.colors.RED
                page.dialog.open = True
                page.update()
                return
        text_msg.controls[0].value = "Enter all fields and tap create"
        text_msg.controls[0].color = flet.colors.BLACK
        page.dialog.open = False
        page.update()

    def get_products():
        client = MongoClient('localhost', 27017)
        db = client['products']
        return db['info']

    def create_table(page, products):
        counter = 0
        table = DataTable(
            columns=[
                DataColumn(Text("N")),
                DataColumn(Text("Name")),
                DataColumn(Text("Type")),
                DataColumn(Text("Description")),
                DataColumn(Text("Comment")),
            ],
        )
        for product in products.find().sort('Name', pymongo.ASCENDING):
            counter += 1
            row = DataRow(
                cells=[
                    DataCell(Text(str(counter))),
                    DataCell(Text(product["Name"])),
                    DataCell(Text(product["Type"]), ),
                    DataCell(Text(product["Description"])),
                    DataCell(Text(product["Comment"])),
                ],
            )
            table.rows.append(row)

        column = Column(
            controls=[
                Container(
                    content=Column(
                        [Row([table], scroll=ScrollMode.ADAPTIVE)],
                        scroll=ScrollMode.ADAPTIVE), expand=1
                ),
                Container(ElevatedButton(text="ADD", on_click=add_new_dialog, expand=0))
            ]
        )
        page.add(SafeArea(column, expand=True))
        page.adaptive = True
        page.update()

    products = get_products()
    create_table(page, products)


# flet.app(target=main, view=flet.AppView.WEB_BROWSER)
# flet.AppView.WEB_BROWSER, web_renderer=ft.WebRenderer.HTML
flet.app(target=main)
