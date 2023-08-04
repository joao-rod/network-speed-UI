import flet as ft
from alert import delete_alert

def homepage(page: ft.Page):
    page.title = "Cadastro de usuário"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.DOWNLOAD_ROUNDED),
                            title=ft.Text("Velocidade de download"),
                            subtitle=ft.Text(
                                "O download é a forma de baixar dados para sua máquina"
                            ),
                        )
                        # Row(
                        #     [TextButton("Ok"), TextButton("Listen")],
                        #     alignment="end",
                        # ),
                    ]
                ),
                width=400,
                padding=10,
                
            ),
        )
    )
    
ft.app(target=homepage)