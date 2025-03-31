import flet as ft

def main(page: ft.Page):
    txtIn = ft.Text(value="Hello, world", color="green")
    # page.controls.append(txtIn)
    # page.update()
    page.add(txtIn)

ft.app(target=main, view=ft.AppView.FLET_APP)