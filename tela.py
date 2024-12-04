from tkinter .ttk import *
from tkinter import *

# cores--------------------

co0 = "#2e2d2b" #preta
co1 = "#feffff" #branca
co2 = "4fa8822" #verde
co3 = "38576b" #valor
co4 = "403d3d" #letra
c05 = "#e06636" # - profit
co6 = "#E9A178"
co7 = "#3fbfb9" #verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = "#6e8faf" #
c11 = "#f2f4f2"


# criando janela------
janela = Tk()
janela.title("")
janela.geometry('770x330')
# janela.configure(background=co1)
# janela.resizable(width=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames------------------

frameCima = Frame(janela, width=770, height=50 , bg=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265 , bg=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265 , bg=co1, relief="raised")
frameDireita.grid(row=1, column=0, sticky=NSEW)


janela.mainloop()
