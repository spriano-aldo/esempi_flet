from time import sleep
import flet as ft

def main(page: ft.Page):

    def button_clicked(e):
        txt.value="Cliccato"
        txt.update()
        sleep(1)
        txt.value=""
        txt.update()

    btn=ft.ElevatedButton(text="Click me", 
                          on_click=button_clicked)
    txt=ft.Text("")
    page.add(btn,txt)

ft.app(target=main, view=ft.AppView.FLET_APP)