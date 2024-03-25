from time import sleep
import flet as ft


def main(page: ft.Page):
    txtIn = ft.Text(value="Buongiorno TdP 2024!", color="red")
    page.controls.append(txtIn)
    page.update()

    # txtOut = ft.Text(value="Counter:", color="red",size=24)
    # page.add(txtOut)

    # for i in range(1,100):
    #     txtOut.value = "Counter: " + str(i)
    #     txtOut.update()
    #     sleep(1)

    def handleBottone(e):
        lv.controls.append(ft.Text("Tasto Cliccato!"))
        lv.update()

    txt1 = ft.Text(value="Colonna 1", color="red")
    txt2 = ft.Text(value="Colonna 2", color="blue")
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleBottone)
    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="red", size=24)
    page.add(row1, txtOut)

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)


ft.app(target=main, view=ft.AppView.FLET_APP)