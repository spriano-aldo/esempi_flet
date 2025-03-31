import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        if dd.value!=None:
            txtout.value = f"Il colore scelto è:  {dd.value}"
            txtout.update()
        else:
            txtout.value="nessuna selezione"
            txtout.update()

    txtout= ft.Text()
    btn = ft.ElevatedButton(text="Submit", 
                            on_click=button_clicked)
    dd = ft.Dropdown( label="colore",
                      width=200,
                      options=[
                                ft.dropdown.Option("Red"),
                                ft.dropdown.Option("Green"),
                                ft.dropdown.Option("Blue"),
                               ],
                    )
    riga=ft.Row([dd, btn])
    page.add(riga, txtout)

ft.app(main)