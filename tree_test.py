import flet as ft
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
)

name = "ExpansionTile example"


def privet(e):
    print("vslkddskljflkdsjfklsjd")


def anim_end(e):
    print("on_animation_end")


def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.ExpansionTile(
                    title=ft.Text("ExpansionTile 1"),
                    subtitle=ft.Text("Trailing expansion arrow icon"),
                    affinity=ft.TileAffinity.PLATFORM,
                    collapsed_text_color=ft.colors.BROWN_900,
                    text_color=ft.colors.BLUE,
                    controls=[

                        ft.ListTile(
                            title=ft.Text("              This is in Panel "),
                            subtitle=ft.Text("                  Press the icon to delete panel "),
                            trailing=ft.IconButton(ft.icons.MORE_VERT, on_click=privet, ),

                        ),
                        ft.ListTile(
                            title=ft.Text("              This is in Panel "),
                            subtitle=ft.Text("                  Press the icon to delete panel "),
                            trailing=ft.IconButton(ft.icons.MORE_VERT, on_click=privet, ),

                        ),
                    ],

                    on_change=privet,
                    on_animation_end=anim_end,
                ),
                # ft.ExpansionTile(
                #     title=ft.Text("ExpansionTile 2"),
                #     subtitle=ft.Text("Custom expansion arrow icon"),
                #     trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
                #     collapsed_text_color=ft.colors.GREEN,
                #     text_color=ft.colors.GREEN,
                #     controls=[ft.ListTile(title=ft.Text("This is sub-tile number 2"))],
                # ),
                ft.ExpansionTile(
                    title=ft.Text("CMT.939.000.0"),
                    subtitle=ft.Text("Шасси  L "),
                    affinity=ft.TileAffinity.PLATFORM,
                    collapsed_text_color=ft.colors.BROWN_900,
                    text_color=ft.colors.BLUE,
                    on_change=privet,
                    controls=[
                        ft.ExpansionTile(
                            title=ft.Text("     CME.1.000.0 "),
                            subtitle=ft.Text("       модуль"),
                            affinity=ft.TileAffinity.PLATFORM,
                            collapsed_text_color=ft.colors.BROWN_900,
                            text_color=ft.colors.BLUE,
                            controls=[ft.ExpansionTile(
                                title=ft.Text("        CMR.39502098.001.1"),
                                subtitle=ft.Text("          Боковина"),
                                affinity=ft.TileAffinity.PLATFORM,
                                collapsed_text_color=ft.colors.BROWN_900,
                                text_color=ft.colors.BLUE,
                                controls=[
                                    # Container(ElevatedButton(text="ADD", expand=20)),
                                    ft.ListTile(
                                        title=ft.Text("              This is in Panel "),
                                        subtitle=ft.Text("                  Press the icon to delete panel "),
                                        trailing=ft.IconButton(ft.icons.MORE_VERT, on_click=privet, ),

                                    ),
                                    ft.ListTile(
                                        title=ft.Text("              This is in Panel "),
                                        subtitle=ft.Text("                  Press the icon to delete panel "),
                                        trailing=ft.IconButton(ft.icons.MORE_VERT, on_click=privet, ),

                                    ),
                                ],
                            ), ],
                        ),
                    ],
                ),
                ft.ExpansionTile(
                    title=ft.Text("ExpansionTile 2"),
                    subtitle=ft.Text("Custom expansion arrow icon"),
                    # affinity=ft.TileAffinity.PLATFORM,
                    collapsed_text_color=ft.colors.BROWN_900,
                    text_color=ft.colors.BLUE,
                    controls=[ft.ListTile(title=ft.Text("This is sub-tile number 2"))],
                ),
            ]
        )
    )


ft.app(target=main)

if __name__ == '__main__':
    main()
