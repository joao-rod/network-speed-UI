import flet as ft


def homepage(page: ft.Page):
    page.title = "Página inicial"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.DataTable(
            bgcolor=ft.colors.GREY_50,
            border=ft.border.all(1, ft.colors.BLUE_GREY_900),
            border_radius=3,
            vertical_lines=ft.border.BorderSide(1, ft.colors.BLUE_GREY_900),
            horizontal_lines=ft.border.BorderSide(1, ft.colors.BLUE_GREY_900),
            sort_column_index=None,
            sort_ascending=False,
            heading_row_color=ft.colors.BLUE_100,
            heading_row_height=50,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=False,
            columns=[
                ft.DataColumn(
                    ft.Text("Data"),
                    tooltip="Data e hora do teste"
                ),
                ft.DataColumn(
                    ft.Text("Local"),
                    tooltip="Local do provedor",
                ),
                ft.DataColumn(
                    ft.Text("Provedor"),
                    tooltip="Provedor de internet",
                ),
                ft.DataColumn(
                    ft.Text("Host"),
                    tooltip="Host",
                ),
                ft.DataColumn(
                    ft.Text("Download"),
                    tooltip="velocidade de download",
                ),
                ft.DataColumn(
                    ft.Text("Upload"),
                    tooltip="velocidade de upload",
                ),
                ft.DataColumn(
                    ft.Text("Latência"),
                    tooltip="Latência da rede",
                )
            ],
            rows=[
                ft.DataRow(
                    [
                        ft.DataCell(ft.Text("2023-08-04 00:35:33")),
                        ft.DataCell(ft.Text("speedtest.brnet.psi.br:8080")),
                        ft.DataCell(ft.Text("BRNET")),
                        ft.DataCell(ft.Text("Ipatinga/BR")),
                        ft.DataCell(ft.Text("57.57")),
                        ft.DataCell(ft.Text("59.72")),
                        ft.DataCell(ft.Text("31.63"))
                    ]
                )
            ],
        )
    )
    
ft.app(target=homepage)