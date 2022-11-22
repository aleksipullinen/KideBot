#!/usr/bin/python3
from tkinter import Tk, ttk, constants
from tkinter import *
from ostobotti import Botti
from ostobotti import Selain

class UI:
    def __init__(self, root):
        self.root = root
        self.botti = Botti()

    def start(self):
        otsikko = ttk.Label(master=self.root, text="Lippujen osto")
        selainNappi = ttk.Button(master= self.root, text ="Avaa selain", command=lambda:Selain.selain(self.botti))
        ostoNappi = ttk.Button(master=self.root, text="Osta liput", command=lambda:Botti.paivita(self.botti))

        otsikko.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        selainNappi.grid(padx=1, pady=5)
        ostoNappi.grid(padx=1, pady=7)
        

window = Tk()
window.title("Kide.app Botti")
window.geometry("400x400")
ui = UI(window)
ui.start()
window.mainloop()

