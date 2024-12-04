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
    c.execute("SELECT * FROM usuarios ")
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
    conn = sqlite3.connect('dados.db')
    query = """
    SELECT livros.titulo, usuarios.nome, emprestimos.data_emprestimo, emprestimos.data_devolucao
    FROM livros
    INNER JOIN emprestimos ON livros.id = emprestimos.id_livro
    INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario
    WHERE emprestimos.data_devolucao IS NULL
    """
    result = conn.execute(query).fetchall()
    conn.close()
    return result


# Função para atualizar a data de devoluçao de emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()  # Estabelece conexão com o banco de dados
    query = """
    UPDATE emprestimos
    SET data_devolucao = ?
    WHERE id = ?
    """
    conn.execute(query, (data_devolucao, id_emprestimo))  # Passa os parâmetros
    conn.commit()  # Confirma as alterações
    conn.close()  # Fecha a conexão

# Testando a função
def inserir_dados_teste():
    conn = sqlite3.connect('dados.db')
    
    # Inserir livros
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('Livro A', 'Autor X', 'Editora Y', 2021, '123456789')")
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('Livro B', 'Autor Y', 'Editora Z', 2020, '987654321')")
    
    # Inserir usuários
    conn.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) VALUES ('João', 'Silva', 'Rua A', 'joao@email.com', '123456789')")
    conn.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) VALUES ('Maria', 'Oliveira', 'Rua B', 'maria@email.com', '987654321')")
    
    # Inserir empréstimos
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (1, 1, '2024-12-01', NULL)")
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (2, 2, '2024-12-02', NULL)")
    
    conn.commit()
    conn.close()

# Inserir dados de teste

# result = get_books_on_loan()
# for i in result: print(i)



