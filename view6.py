#codigo referentevao video 12/12 feito pela Gabrielle e Giselly
import  sqlite3

#Conectar ao banco de dados 
def connect():
    con = sqlite3.connect('dados.db')
    return con

# Função para inserir um novo livro
def insert_book (titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) \
                  VALUES (?, ?, ?, ?, ?)",(titulo, autor, editora, ano_publicacao, isbn)) 

    conn.commit()
    conn.close()

# def para inserir usuário
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios)
    users = c.fetchall()
    conn.close()
    return users


# Função para inserir usuários
def insert_user(nome, sobrenome, endereco, email,telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email,telefone) \
                  VALUES(?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email,telefone))
    conn.commit()
    conn.close()

# Funcao para exibir usuarios
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Função para exibir livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM  livros").fetchall()
    conn.close()

    return livros



# Função para realizar emprestimos 
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute(" INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) \
                   VALUES(?,?,?,?)", (id_livro, id_usuario, data_emprestimo,data_devolucao))

    conn.commit()
    conn.close()

# Função para recuperar todos o livros emprestados no momento 

def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, empretimos.data_devolucao \
                            FROM livros\
                            INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                            INNER JOIN usuarios ON usuario.id = emprestimos.id_usuario\
                            WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result



# Função para atualizar a data de devoluçao de emprestimo
def update_loan_return_date(data_devolucao,id_emprestimo):
    conn = connect()
    conn.execute(" UPDATE emprestimos SET data_devolucao = ? id = ?", (id_emprestimo, data_devolucao))
    conn.commit()
    conn.close()