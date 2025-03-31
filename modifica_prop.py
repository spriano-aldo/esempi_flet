#in questo programma si aggiorna il valore di un campo testo
import time
import flet as ft

def main(page:ft.Page):
    titolo=ft.Text("Aggiornamento,campo di testo",size=30,color="blue")
    # si istanzia un campo di testo
    t = ft.Text(color="red",size=20)
    #si aggiunge alla lista dei controlli e si aggiorna la pagina
    page.add(titolo,t)

    # con un ciclo for si modifica il valore del campo e 
    # si aggiorna ad ogni iterazione
    for i in range(10):
        t.value = f"Contatore {i}"
        t.update()
        time.sleep(1)
  
    # è anche possibile modificare uno degli attributi
    # di un controllo
    t.size=40
    t.update()


ft.app(main)