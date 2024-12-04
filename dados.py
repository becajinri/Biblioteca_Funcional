# O Nome do arquivo inicial é dados.py  1/12

import  sqlite3

#Conectar ao banco de dados ou criar um novo banco de dados :)
con = sqlite3.connect('dados.db')

# # Criar uma tabela de livros e execute pra executar comandos em sql
con.execute('CREATE TABLE livros(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INT,\
                isbn TEXT)')

# Criando tabela de Usuários
con.execute('CREATE TABLE usuarios(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# Criando tabela de Empréstimos
con.execute('CREATE TABLE emprestimos(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                id_livro INT,\
                id_usuario INT,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')
con.commit()
con.close