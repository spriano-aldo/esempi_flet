import flet as ft

def main(page: ft.Page):
    txt1 = ft.Text(value="colonna1", color="blue", size=20)
    txt2 = ft.Text(value="colonna2", color="blue", size=20)
    txt3 = ft.Text(value="colonna3", color="blue", size=20)
    r=ft.Row([txt1,txt2,txt3])
    page.add(r)

ft.app(target=main, view=ft.AppView.FLET_APP)