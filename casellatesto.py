import flet as ft

def main(page: ft.Page):
    # funzione che gestisce la pressione del bottone
    # scrive nella casella di testo il saluto al nome
    # scritto nel textField
    def saluta(e):
        t.value=f"Benvenuto {tb1.value}"
        # dopo la scrittura cancella tb1 altrimenti rimane 
        # il nome scritto in precedenza
        tb1.value="" 
        tb1.update()
        t.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Inserisci il nome")
    btn = ft.ElevatedButton(text="Submit", on_click=saluta)
    riga=ft.Row([tb1 , btn])
    page.add(riga,t)

ft.app(target=main)