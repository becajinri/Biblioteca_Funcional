# Código referente a continuação do código do vídeo 7 e 8 feito pela Gabrielle 8/12

from tkinter .ttk import *
from tkinter import *
from tkinter import tk, ttk
from PIL import Image, ImageTK

from tkinter import messagebox

# importando as funcoes da view
frow view import *

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

style = Style (janela)
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


# novo usuario

def novo_usuario():

    

    global img_salvar

    

    def add():

        first_name = e_p_nome.get()

        last_name = e_sobrenome.get()

        address = e_email.get()

        phone = e_numero.get()

        

        lista = [first_name, last_name, address, email, phone]

        

        # Verificando caso algum campo esteja vazio ou nao

        for i in lista:

            if i== '':

                messagebox.showerror('erro', 'Preencha todos os campos')

                return

                

        # inserindo os dados no banco de dados

        insert_user(first_name, last_name, address, email, phone)

        

        messagebox.showinfo('Sucesso', 'Usuario incerido com sucesso')

        

        #limpando os campos de entrada

        e_p_nome.delete(0,END)

        e_sobrenome.delete(0,END)

        e_endereco.delete(0,END) # type: ignore

        e_email.delete(0,END)

        e_numero.delete(0,END)

    

    app_ = Label(frameDireita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('verdana 12'), bg=co1, fg=co4)

    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_Linha = Label(frameDireita, width=400, height=1, anchor= NW, font= ('verdana 1') , bg= co3, fg=co1)
    app_Linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
     
    l_p_nome = Label(frameDireita, text="Primeiro nome*",anchor= NW, font=('Ivy 10'), bg=co1, fg=co4)

    l_p_nome.grid(row=2, column=0, padx=5, pady=5,sticky=NSEW)
    e_p_nome = Entry(frameDireita, width=25, justify='left', relief='solid')

    e_p_nome.grid(row=2, column=1, padx=5, pady=5,sticky=NSEW)

    

    l_sobrenome = Label(frameDireita, text="Sobrenome*",anchor= NW, font=('Ivy 10'), bg=co1, fg=co4)

    l_sobrenome.grid(row=3, column=0, padx=5, pady=5,sticky=NSEW)
    e_sobrenome = Entry(frameDireita, width=25, justify='left', relief='solid')

    e_sobrenome.grid(row=3, column=1, padx=5, pady=5,sticky=NSEW)

    

    l_endereco = Label(frameDireita, text="Endereço do usuário*",anchor= NW, font=('Ivy 10'), bg=co1, fg=co4)

    l_endereco.grid(row=4, column=0, padx=5, pady=5,sticky=NSEW)

    e_endereco= Entry(frameDireita, width=25, justify='left', relief='solid')

    e_endereco.grid(row=4, column=1, padx=5, pady=5,sticky=NSEW)

    

    l_email = Label(frameDireita, text="Endereço de email*",anchor= NW, font=('Ivy 10'), bg=co1, fg=co4)

    l_email.grid(row=5, column=0, padx=5, pady=5,sticky=NSEW)
    e_email = Entry(frameDireita, width=25, justify='left', relief='solid')

    e_email.grid(row=5, column=1, padx=5, pady=5,sticky=NSEW)

    

    l_numero = Label(frameDireita, text="Numero de telefone*",anchor= NW, font=('Ivy 10'), bg=co1, fg=co4)

    l_numero.grid(row=6, column=0, padx=5, pady=5,sticky=NSEW)
    e_numero = Entry(frameDireita, width=25, justify='left', relief='solid')

    e_numero.grid(row=6, column=1, padx=5, pady=5,sticky=NSEW)
     


    # Botao salvar
    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTK.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar,compound= LEFT, width=100, anchor=NW, text= ' Salvar ', bg=co1, fg=co4, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
    b_salvar.grid(row=7, column=1,sticky=NSEW,padx=5,pady=6)



# Ver usuarios

def ver_usuarios():

    

    app_ = Label(frameDireita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=('verdana 12'), bg=co1, fg=co4)

    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_Linha = Label(frameDireita, width=400, height=1, anchor= NW, font= ('verdana 1') , bg= co3, fg=co1)
    app_Linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
     
    dados = get_users()
     
    #creating a treeview with dual scrollbars
    list_header =['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
                        
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n],anchor=hd[n])
         
        n+=1
         
    for item in dados:
        tree.insert('', 'end', values=item)


# Funcao para controlar o menu -------------


def control(i):

    

    # novo usuario

    if i == 'novo_usuario':

        for widget in frameDireita.winfo_children():

            widget.destroy

            

        # chamando a funcao novo usuario 

        novo_usuario()

         

    # novo usuario

    if i == 'ver_usuarios':

        for widget in frameDireita.winfo_children():

            widget.destroy

            

        # chamando a funcao novo usuario

        ver_usuarios()    



#Menu----------

# Novo usuario
img_usuario = Image.open('add.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTK.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=Lambda:control('novo_usuario'),image=img_usuario,compound= LEFT, anchor=NW, text= ' Novo usuario', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_usuario.grid(row=0, column=0,sticky=NSEW,padx=5,pady=6)


# Novo Livro
img_novo_livro = Image.open('add.png')
img_novo_livro = img_novo_livro.resize((18,18))
img_novo_livro = ImageTK.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda,image=img_novo_livro,compound= LEFT, anchor=NW, text= ' Novo Livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
b_novo_livro.grid(row=1, column=0,sticky=NSEW,padx=5,pady=6)

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
b_ver_usuario = Button(frameEsquerda, command=Lambda:control('ver_usuarios'),image=img_usuario,compound= LEFT, anchor=NW, text= ' Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief= RIDGE, relief=GROOVE )
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
