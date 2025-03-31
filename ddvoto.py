import flet as ft

def main(page: ft.Page):

    def button_clicked(e):
        if ddVoto.value!=None:
            txtout.value = f"il voto è:  {ddVoto.value}"
            txtout.update()
        else:
            txtout.value="nessuna selezione"
            txtout.update()

    def fillDdVoto():
        # si definisce una lista vuota in cui caricare
        # le opzioni
        opzioni=[] 
        for i in range(18,31):
            # ad ogni ciclo si appende un'opzione alla lista
            # l'opzione è ft.dropdown.Option(str(i)
            opzioni.append(ft.dropdown.Option(str(i)))
        opzioni.append(ft.dropdown.Option("30L"))
        # Lafunzione ritorna la lista compilata opzioni
        return opzioni

    # ft.Dropdown ha la proprità opzions, a cui la 
    # funzione restituisce la lista costruita opzioni
    ddVoto = ft.Dropdown(label="Voto",width=150,
                         options=fillDdVoto())
    
    btn = ft.ElevatedButton(text="Submit", 
                            on_click=button_clicked)
    txtout= ft.Text()
    riga=ft.Row([ddVoto, btn])
    page.add(riga, txtout)
    
   
ft.app(target=main, view=ft.AppView.FLET_APP)