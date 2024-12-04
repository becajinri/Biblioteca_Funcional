## Código referente a continuação do código do vídeo 6 feito pela Giselly 6/12

from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTK


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
janela.configure(background=co1)
janela.resizable(width=FALSE)

style = style (janela)
style.theme_use("clam")

# Frames------------------
frameCima = Frame(janela, width=770, height=50 , bd=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265 , bd=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265 , bd=co1, relief="raised")
frameDireita.grid(row=1, column=0, sticky=NSEW)

#logo-----

# abrindo a imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTK.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000,compound=LEFT, padx=5,anchor=NW, bg=co6, fg= co1)
app_logo.place(x=5,y=0)

app_ = Label(frameCima, text= Sistema de Gerenciamento de Livros, compound= LEFT, padx= 5, anchor= NW, font= ('verdana 15 bold') , bg= co6, fg=co1)
app_.place(x=50,y=7)

app_Linha = Label(frameCima, width=770, height=1, padx= 5, anchor= NW, font= ('verdana 1') , bg= co3, fg=co1)
app_Linha.place(x=0,y=47)

#Menu----------

# Novo usuario
img_usuario = Image.open('add.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTK.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda,image=img_usuario,compound= LEFT, anchor=NW, text= ' Novo usuario', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_usuario.grid(row=0, column=0,sticky=NSEW,padx=5,pady=6)

# Ver livros
img_ver_livros = Image.open('logo.png')
img_ver_livros = img_ver_livros.resize((18,18))
img_ver_livros = ImageTK.PhotoImage(img_ver_livros)
b_ver_livros = Button(frameEsquerda,image=img_usuario,compound= LEFT, anchor=NW, text= ' Exibir todos os livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_ver_livros.grid(row=2, column=0,sticky=NSEW,padx=5,pady=6)

# Ver usuarios 
img_ver_usuario = Image.open('user.png')
img_ver_usuario = img_ver_livros.resize((18,18))
img_ver_usuario = ImageTK.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda,image=img_usuario,compound= LEFT, anchor=NW, text= ' Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_ver_usuario.grid(row=3, column=0,sticky=NSEW,padx=5,pady=6)

# Realizar um emprestimo 
img_imprestimo = Image.open('add.png')
img_imprestimo = img_ver_livros.resize((18,18))
img_imprestimo = ImageTK.PhotoImage(img_ver_usuario)
b_imprestimo = Button(frameEsquerda,image=img_usuario,compound= LEFT, anchor=NW, text='Realizar um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_imprestimo.grid(row=3, column=0,sticky=NSEW,padx=5,pady=6)

# Devolucao de um emprestimo 
img_devolucao = Image.open('devolucao.png')
img_devolucao = img_devolucao.resize((18,18))
img_devolucao = ImageTK.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda,image=img_usuario,compound= LEFT, anchor=NW, text='Devolucao de um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_devolucao.grid(row=4, column=0,sticky=NSEW,padx=5,pady=6)

# Livros emprestados no momento
img__livros_emprestados = Image.open('livros2.png')
img__livros_emprestados = img_devolucao.resize((18,18))
img__livros_emprestados = ImageTK.PhotoImage(img_devolucao)
b_livros_emprestados = Button(frameEsquerda,image=img_usuario,compound= LEFT, anchor=NW, text='Livros emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_livros_emprestados.grid(row=4, column=0,sticky=NSEW,padx=5,pady=6)


janela.mainloop()
