#Dicionário com todos os usários do jogo
usuarios = {

  1: {
    "nome": "Tiago",
    "sobrenome": "Santos",
    "email": "tiago@gmail.com",
    "idade": 23,
    "cidade": "Salvador",
    "senha": "1234",
    "imagem": "/static/img/perfil_6.png"
  },

  2:{
    "nome": "Ana",
    "sobrenome": "Oliveira",
    "email": "ana@gmail.com",
    "idade": 25,
    "cidade": "Fortaleza",
    "senha": "1234",
    "imagem": "/static/img/perfil_2.png"
  },

  3:{
    "nome": "Ester",
    "sobrenome": "Santana",
    "email": "ester@gmail.com",
    "idade": 27,
    "cidade": "Belo Horizonte",
    "senha": "1234",
    "imagem": "/static/img/perfil_5.png"
  },

  4:{
    "nome": "Luiza",
    "sobrenome": "Andrade",
    "email": "luiza@gmail.com",
    "idade": 38,
    "cidade": "Rio de Janeiro",
    "senha": "1234",
    "imagem": "/static/img/perfil_4.png"
  },

  5:{
    "nome": "Carlos",
    "sobrenome": "Miranda",
    "email": "carlos@gmail.com",
    "idade": 37,
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
def criar_usuario(nome, sobrenome, email, idade, cidade, senha):
    usuarios[gerar_id()] = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "idade": idade,
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
    