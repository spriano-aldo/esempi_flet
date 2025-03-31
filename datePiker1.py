import datetime
import flet as ft

def main(page: ft.Page):
    page.title = "DatePicker"

    # Campo di testo per mostrare la data selezionata
    txtData = ft.Text("")

    # Funzione chiamata quando l'utente sceglie una data
    def on_date_selected(e):
        if dp.value:
             # Aggiorna il campo di testo
            txtData.value = str(dp.value.strftime('%Y-%m-%d')) 
            txtData.update()  # Aggiorna l'interfaccia

    def handle_dismissal(e):
        txtData.value="DatePicker dismissed"
        txtData.update()  # Aggiorna l'interfaccia
    
    # Creiamo il DatePicker
    dp = ft.DatePicker(
                    first_date=datetime.datetime(year=2023, month=10, day=1),
                    last_date=datetime.datetime(year=2025, month=6, day=16),
                    on_change=on_date_selected,
                    on_dismiss=handle_dismissal,
                )
    # Funzione per aprire il DatePicker, richiede il metodo open() page
    def apri_dp(e):
        page.open(dp) # Questo apre il DatePicker

    # Bottone per aprire il DatePicker
    btn_seleziona = ft.ElevatedButton("Seleziona data", 
                                      icon=ft.Icons.CALENDAR_MONTH,
                                      on_click=apri_dp)

    # Aggiungiamo tutto alla pagina
    page.add(btn_seleziona, dp, txtData)

ft.app(target=main)