import flet as ft


def delete_alert(page: ft.Page):
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Atenção"),
        content=ft.Text("Deseja realmente excluir o registro?"),
        actions=[
            ft.TextButton("Sim", on_click=close_dlg), # Deletar registro
            ft.TextButton("Não", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    page.add(
        ft.ElevatedButton(
            height=25,
            width=120,
            icon=ft.icons.DELETE_ROUNDED, 
            icon_color=ft.colors.RED, 
            text="Excluir",
            tooltip="Excluir registro",
            bgcolor=ft.colors.GREY_50,
            on_click=open_dlg_modal
        ),
    )
    
    # Utilizando o Row para organizar os botões
    # page.add(
    #     ft.ElevatedButton(
    #         width=120,
    #         content=ft.Row(
    #             [ft.Icon(name=ft.icons.DELETE, color="RED"), ft.Text("Excluir")]
    #         ),
    #         on_click=open_dlg_modal
    #     ),
    # )

