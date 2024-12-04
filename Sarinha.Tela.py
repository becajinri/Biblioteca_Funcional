from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from corrigidoSarinha import insert_user, get_users, update_loan_return_date, get_books_on_loan, insert_loan  # Ajuste conforme necessário
from tkinter import messagebox
from datetime import *
import sqlite3

# Definir as cores
co1 = "#feffff"  # Branco
co4 = "#403d3d"  # Cinza escuro
co6 = "#E9A178"  # Bege
co3 = "#38576b"  # Azul

# Configurando a janela principal
janela = Tk()
janela.title("Sistema de Gerenciamento de Livros")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=True, height=False)

# Estilo
style = ttk.Style(janela)
style.theme_use("clam")

# Frames
frameCima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Logo
try:
    app_img = Image.open('logo.png')
    app_img = app_img.resize((40, 40))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, anchor=NW, bg=co6)
    app_logo.place(x=5, y=0)
except Exception as e:
    print(f"Erro ao carregar a imagem 'logo.png': {e}")

# Título
app_title = Label(frameCima, text="Sistema de Gerenciamento de Livros", font=('verdana 15 bold'), bg=co6, fg=co1)
app_title.place(x=50, y=7)

# Linha decorativa
app_linha = Label(frameCima, width=770, height=1, bg=co3)
app_linha.place(x=0, y=47)

# Função para adicionar novo usuário
def novo_usuario():
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Novo Usuário", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=2, pady=10)

    # Campos
    Label(frameDireita, text="Primeiro Nome:", bg=co1).grid(row=1, column=0, padx=10, sticky=E)
    nome_entry = Entry(frameDireita)
    nome_entry.grid(row=1, column=1, padx=10)

    Label(frameDireita, text="Sobrenome:", bg=co1).grid(row=2, column=0, padx=10, sticky=E)
    sobrenome_entry = Entry(frameDireita)
    sobrenome_entry.grid(row=2, column=1, padx=10)

    Label(frameDireita, text="Endereço:", bg=co1).grid(row=3, column=0, padx=10, sticky=E)
    endereco_entry = Entry(frameDireita)
    endereco_entry.grid(row=3, column=1, padx=10)

    Label(frameDireita, text="Email:", bg=co1).grid(row=4, column=0, padx=10, sticky=E)
    email_entry = Entry(frameDireita)
    email_entry.grid(row=4, column=1, padx=10)

    Label(frameDireita, text="Telefone:", bg=co1).grid(row=5, column=0, padx=10, sticky=E)
    telefone_entry = Entry(frameDireita)
    telefone_entry.grid(row=5, column=1, padx=10)

    # Botão Salvar
    def salvar():
        # Validação e salvamento
        if nome_entry.get() and sobrenome_entry.get():
            insert_user(nome_entry.get(), sobrenome_entry.get(), endereco_entry.get(), email_entry.get(), telefone_entry.get())
            messagebox.showinfo("Sucesso", "Usuário salvo com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")

    Button(frameDireita, text="Salvar", command=salvar, bg=co6, fg=co1).grid(row=6, column=0, columnspan=2, pady=10)

def devolucao_emprestimo():
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Devolução de Empréstimo", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=2, pady=10)

    # Campo para ID do empréstimo
    Label(frameDireita, text="ID do Empréstimo:", bg=co1).grid(row=1, column=0, padx=10, sticky=E)
    id_emprestimo_entry = Entry(frameDireita)
    id_emprestimo_entry.grid(row=1, column=1, padx=10)

    # Campo para nova data de devolução
    Label(frameDireita, text="Data de Devolução (AAAA-MM-DD):", bg=co1).grid(row=2, column=0, padx=10, sticky=E)
    data_retorno_entry = Entry(frameDireita)
    data_retorno_entry.grid(row=2, column=1, padx=10)

    # Botão para atualizar a devolução
    def atualizar_devolucao():
        loan_id = id_emprestimo_entry.get()
        return_date = data_retorno_entry.get()

        if loan_id and return_date:
            try:
                update_loan_return_date(loan_id, return_date)
                messagebox.showinfo("Sucesso", "Devolução registrada com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao registrar devolução: {e}")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    Button(frameDireita, text="Atualizar", command=atualizar_devolucao, bg=co6, fg=co1).grid(row=3, column=0, columnspan=2, pady=10)

def ver_livros_emprestados():
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Livros Emprestados no Momento", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=4, pady=10)

    dados = get_books_on_loan()  # Recuperar os dados do banco

    # Cabeçalhos para a TreeView
    list_header = ['ID Empréstimo', 'Título do Livro', 'Nome do Usuário', 'Data Empréstimo', 'Data Devolução']

    # Criar TreeView
    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    tree.grid(row=1, column=0, columnspan=4, sticky='nsew')

    # Scrollbars
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    vsb.grid(row=1, column=4, sticky='ns')
    hsb.grid(row=2, column=0, columnspan=4, sticky='ew')

    # Configurar as colunas
    for col in list_header:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, width=100, anchor='center')

    # Inserir os dados
    for item in dados:
        tree.insert('', 'end', values=item)

def realizar_emprestimo():
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Realizar Empréstimo", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=2, pady=10)

    # Campos de entrada
    Label(frameDireita, text="ID do Usuário:", bg=co1).grid(row=1, column=0, padx=10, sticky=E)
    id_usuario_entry = Entry(frameDireita)
    id_usuario_entry.grid(row=1, column=1, padx=10)

    Label(frameDireita, text="ID do Livro:", bg=co1).grid(row=2, column=0, padx=10, sticky=E)
    id_livro_entry = Entry(frameDireita)
    id_livro_entry.grid(row=2, column=1, padx=10)

    # Botão para registrar empréstimo
    def registrar_emprestimo():
        user_id = id_usuario_entry.get()
        book_id = id_livro_entry.get()

        if user_id and book_id:
            try:
                insert_loan(user_id, book_id, datetime.today().strftime('%Y-%m-%d'), None)
                messagebox.showinfo("Sucesso", "Empréstimo registrado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao registrar empréstimo: {e}")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    Button(frameDireita, text="Registrar", command=registrar_emprestimo, bg=co6, fg=co1).grid(row=3, column=0, columnspan=2, pady=10)



def ver_usuarios():
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Usuários Cadastrados", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=4, pady=10)

    dados = get_users()  # Função que retorna os usuários

    tree = ttk.Treeview(frameDireita, columns=("ID", "Nome", "Sobrenome"), show="headings")
    tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Sobrenome", text="Sobrenome")

    for user in dados:
        tree.insert('', 'end', values=user)

def ver_livros_emprestados():
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Livros Emprestados", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=4, pady=10)

    dados = get_books_on_loan()  # Recupera os dados dos empréstimos

    tree = ttk.Treeview(frameDireita, columns=("Título", "Usuário", "Data Empréstimo", "Data Devolução"), show="headings")
    tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

    tree.heading("Título", text="Título")
    tree.heading("Usuário", text="Usuário")
    tree.heading("Data Empréstimo", text="Data Empréstimo")
    tree.heading("Data Devolução", text="Data Devolução")

    for loan in dados:
        tree.insert('', 'end', values=loan)

def novo_livro():
    # Limpa os widgets do frameDireita
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Novo Livro", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=2, pady=10)

    # Campos de entrada
    Label(frameDireita, text="Título:", bg=co1).grid(row=1, column=0, padx=10, sticky=E)
    titulo_entry = Entry(frameDireita)
    titulo_entry.grid(row=1, column=1, padx=10)

    Label(frameDireita, text="Autor:", bg=co1).grid(row=2, column=0, padx=10, sticky=E)
    autor_entry = Entry(frameDireita)
    autor_entry.grid(row=2, column=1, padx=10)

    Label(frameDireita, text="Editora:", bg=co1).grid(row=3, column=0, padx=10, sticky=E)
    editora_entry = Entry(frameDireita)
    editora_entry.grid(row=3, column=1, padx=10)

    Label(frameDireita, text="Ano de Publicação:", bg=co1).grid(row=4, column=0, padx=10, sticky=E)
    ano_entry = Entry(frameDireita)
    ano_entry.grid(row=4, column=1, padx=10)

    Label(frameDireita, text="ISBN:", bg=co1).grid(row=5, column=0, padx=10, sticky=E)
    isbn_entry = Entry(frameDireita)
    isbn_entry.grid(row=5, column=1, padx=10)

    # Botão para salvar o livro
    def salvar():
        titulo = titulo_entry.get()
        autor = autor_entry.get()
        editora = editora_entry.get()
        ano = ano_entry.get()
        isbn = isbn_entry.get()

        if titulo and autor and editora and ano.isdigit() and isbn:
            try:
                conn = sqlite3.connect('dados.db')
                conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                             (titulo, autor, editora, int(ano), isbn))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucesso", "Livro salvo com sucesso!")
                # Limpar os campos
                titulo_entry.delete(0, END)
                autor_entry.delete(0, END)
                editora_entry.delete(0, END)
                ano_entry.delete(0, END)
                isbn_entry.delete(0, END)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar o livro: {e}")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

    Button(frameDireita, text="Salvar", command=salvar, bg=co6, fg=co1).grid(row=6, column=0, columnspan=2, pady=10)

def ver_livros():
    # Limpa os widgets do frameDireita
    for widget in frameDireita.winfo_children():
        widget.destroy()

    Label(frameDireita, text="Livros Cadastrados", font=('verdana 12'), bg=co1, fg=co4).grid(row=0, column=0, columnspan=4, pady=10)

    # Obter dados dos livros
    try:
        conn = sqlite3.connect('dados.db')
        dados = conn.execute("SELECT id, titulo, autor, editora, ano_publicacao, isbn FROM livros").fetchall()
        conn.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar livros: {e}")
        return

    # Configurar TreeView
    tree = ttk.Treeview(frameDireita, columns=("ID", "Título", "Autor", "Editora", "Ano", "ISBN"), show="headings")
    tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

    tree.heading("ID", text="ID")
    tree.heading("Título", text="Título")
    tree.heading("Autor", text="Autor")
    tree.heading("Editora", text="Editora")
    tree.heading("Ano", text="Ano")
    tree.heading("ISBN", text="ISBN")

    # Ajustar larguras das colunas
    tree.column("ID", width=50, anchor="center")
    tree.column("Título", width=150, anchor="w")
    tree.column("Autor", width=100, anchor="w")
    tree.column("Editora", width=100, anchor="w")
    tree.column("Ano", width=50, anchor="center")
    tree.column("ISBN", width=100, anchor="center")

    # Inserir dados no TreeView
    for livro in dados:
        tree.insert("", "end", values=livro)

    # Scrollbars
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    vsb.grid(row=1, column=4, sticky="ns")
    hsb.grid(row=2, column=0, columnspan=4, sticky="ew")


def control(i):
    # Limpa os widgets do frameDireita antes de carregar a próxima interface
    for widget in frameDireita.winfo_children():
        widget.destroy()

    # Chamadas para as funções correspondentes
    if i == 'novo_usuario':
        novo_usuario()

    elif i == 'ver_usuarios':
        ver_usuarios()

    elif i == 'novo_livro':
        novo_livro()

    elif i == 'ver_livros':
        ver_livros()

    elif i == 'emprestimo':
        realizar_emprestimo()

    elif i == 'ver_livros_emprestados':
        ver_livros_emprestados()

    elif i == 'retorno':
        devolucao_emprestimo()


# Botão de exemplo no menu
Button(frameEsquerda, text="Novo Usuário", command=novo_usuario, bg=co4, fg=co1).grid(row=0, column=0, padx=5, pady=5)
b_novo_usuario = Button(frameEsquerda, text="Novo Usuário", command=lambda: control('novo_usuario'), bg=co4, fg=co1)
b_novo_usuario.grid(row=0, column=0, padx=5, pady=5)

b_ver_usuarios = Button(frameEsquerda, text="Ver Usuários", command=lambda: control('ver_usuarios'), bg=co4, fg=co1)
b_ver_usuarios.grid(row=1, column=0, padx=5, pady=5)

b_novo_livro = Button(frameEsquerda, text="Novo Livro", command=lambda: control('novo_livro'), bg=co4, fg=co1)
b_novo_livro.grid(row=2, column=0, padx=5, pady=5)

b_ver_livros = Button(frameEsquerda, text="Ver Livros", command=lambda: control('ver_livros'), bg=co4, fg=co1)
b_ver_livros.grid(row=3, column=0, padx=5, pady=5)

b_realizar_emprestimo = Button(frameEsquerda, text="Realizar Empréstimo", command=lambda: control('emprestimo'), bg=co4, fg=co1)
b_realizar_emprestimo.grid(row=4, column=0, padx=5, pady=5)

b_ver_emprestados = Button(frameEsquerda, text="Livros Emprestados", command=lambda: control('ver_livros_emprestados'), bg=co4, fg=co1)
b_ver_emprestados.grid(row=5, column=0, padx=5, pady=5)

b_devolucao = Button(frameEsquerda, text="Registrar Devolução", command=lambda: control('retorno'), bg=co4, fg=co1)
b_devolucao.grid(row=6, column=0, padx=5, pady=5)

b_novo_livro = Button(frameEsquerda, text="Novo Livro", command=lambda: control('novo_livro'), bg=co4, fg=co1)
b_novo_livro.grid(row=2, column=0, padx=5, pady=5)




# Finalização
janela.mainloop()
