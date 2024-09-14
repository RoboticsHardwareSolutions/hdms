import flet as ft


def main(page):
    table = ft.DataTable(
        border=ft.border.all(1, "red"),
        show_bottom_border=True,
        columns=[
            ft.DataColumn(ft.Text("名字")),
            ft.DataColumn(ft.Text("电话")),
            ft.DataColumn(ft.Text("地址"), numeric=True),
        ],

        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Johnew0-opiopwepo\nripw")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John"), show_edit_icon=True),
                ])
        ]
    )
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    lv.controls.append(table)
    page.add(lv)

    def button_clicked(e):
        b = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text("John")),
                ft.DataCell(ft.Text("John")),
                ft.DataCell(ft.Text("John\ndspiklgskdl")),
            ])

        table.rows.append(b)
        page.update()
        print("按钮被点击")

    page.add(ft.ElevatedButton(text="ADD", on_click=button_clicked, data=0))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
