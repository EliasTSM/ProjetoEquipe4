import sqlite3

conexao = sqlite3.connect('cadastro.db')

def gerir_id():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='email'")
    next_id = cursor.fetchone()[0]
    return next_id + 1
# nome, sobrenome, email, idade, cidade, senha
def criar_cadastro(nome, sobrenome, email, idade, cidade, senha):
    try:
        conexao = sqlite3.connect('cadastro.db')
        cursor = conexao.cursor()
        sql_insert = "INSERT INTO cadastro (nome_usuario, sobrenome_usuario, email_usuario, idade_usuario, cidade_usuario, senha_usuario) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, sobrenome, email, idade, cidade, senha))
        id_usuario = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return id_usuario
    except Exception as Ex:
        print(Ex)
        return 0
    
def atualizar_cadastro(id:int, nome, sobrenome, email, idade, cidade, senha):
    try:
        conexao = sqlite3.connect('cadastro.db')
        cursor = conexao.cursor()
        sql_update = "UPDATE cadastro SET nome_usuario = ?, sobrenome_usuario = ?, email_usuario = ?, idade_usuario = ?, cidade_usuario = ?, senha_usuario = ? WHERE id_usuario = ?"
        cursor.execute(sql_update, (nome, sobrenome, email, idade, cidade, senha))
        conexao.commit()
        conexao.close()
        return True
    except Exception as Ex:
        print(Ex)
        return False

def remover_cadastro(id:int):
    try:
        conexao = sqlite3.connect('cadastro.db')
        cursor = conexao.cursor()
        sql_remove = "DELETE FROM cadastro WHERE id_usuario = ?"
        cursor.execute(sql_remove, (id, ))
        conexao.commit()
        conexao.close()
        return True
    except Exception as Ex:
        print(Ex)
        return False
    
def retornar_cadastro(id:int):
    try:
        if id == 0:
            return gerir_id(), "", "", "", "", "", ""        
        conexao = sqlite3.connect('cadastro.db')
        cursor = conexao.cursor()

        sql_select = "SELECT * FROM cadastro WHERE id_usuario = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, sobrenome, email, idade, cidade, senha = cursor.fetchone()
        conexao.close()
        return id, nome, sobrenome, email, idade, cidade, senha
    except:
        return False
    
def retornar_cadastros():
    try:
        conexao = sqlite3.connect('cadastro.db')
        cursor = conexao.cursor()
        sql_select = "SELECT * FROM cadastro"
        cursor.execute(sql_select)
        cadastros = cursor.fetchall()
        conexao.close()
        return cadastros
    except:
        return False
    
        
