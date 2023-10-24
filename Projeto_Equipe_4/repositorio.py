#Dicionário com todos os usários do jogo
usuarios = {

  1: {
    "nome": "Tiago",
    "sobrenome": "Santos",
    "email": "tiago@gmail.com",
    "nascimento": "12/01/1999",
    "cidade": "Salvador",
    "senha": "1234",
    "imagem": "/static/img/perfil_6.png"
  },

  2:{
    "nome": "Ana",
    "sobrenome": "Oliveira",
    "email": "ana@gmail.com",
    "nascimento": "12/08/1998",
    "cidade": "Fortaleza",
    "senha": "1234",
    "imagem": "/static/img/perfil_2.png"
  },

  3:{
    "nome": "Ester",
    "sobrenome": "Santana",
    "email": "ester@gmail.com",
    "nascimento": "17/10/1995",
    "cidade": "Belo Horizonte",
    "senha": "1234",
    "imagem": "/static/img/perfil_5.png"
  },

  4:{
    "nome": "Luiza",
    "sobrenome": "Andrade",
    "email": "luiza@gmail.com",
    "nascimento": "27/03/1985",
    "cidade": "Rio de Janeiro",
    "senha": "1234",
    "imagem": "/static/img/perfil_4.png"
  },

  5:{
    "nome": "Carlos",
    "sobrenome": "Miranda",
    "email": "carlos@gmail.com",
    "nascimento": "09/03/1986",
    "cidade": "São Paulo",
    "senha": "1234",
    "imagem": "/static/img/perfil_7.png"
  }

}

#Gera um ID
def gerar_id():
    id = len(usuarios) + 1
    return id

#Cria um usuário
def criar_usuario(nome, sobrenome, email, nasciemnto, cidade, senha):
    usuarios[gerar_id()] = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "nascimento": nasciemnto,
        "cidade": cidade,
        "senha": senha
    }

#Retorna todos os usuários
def retornar_usuarios():
    return usuarios

#Retorna um usuário unico
def retornar_usuario(id: int):
    if id in usuarios.keys():
        return usuarios[id]
    else:
        return {}

#Atualiza informações de um usuário 
def atualizar_usuario(id: int, dados_usuario: dict):
    usuarios[id] = dados_usuario

#Exclui um usuário
def remover_usuario(id: int):
    del usuarios[id]
    