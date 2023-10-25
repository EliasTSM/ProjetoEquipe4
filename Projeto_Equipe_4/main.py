from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        usuarios = repositorio.retornar_usuarios()
        for id, usuario in usuarios.items():
            if usuario['email'] == request.form["email"]:
                if usuario['senha'] == request.form["senha"]:
                  return redirect(url_for("perfil", id=id))  
    else:
        return render_template("login.html")


@app.route("/cadastro", methods = ['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        usuario = {}
        usuario['nome'] = request.form["nome"]
        usuario['sobrenome'] = request.form["sobrenome"]
        usuario['email'] = request.form["email"]
        usuario['idade'] = request.form["idade"]
        usuario['cidade'] = request.form["cidade"]
        usuario['senha'] = request.form["senha"]
        repositorio.criar_usuario(**usuario)
        return redirect(url_for('login'))
    else:
        return render_template("cadastro.html")


@app.route("/perfil/<int:id>", methods = ['GET', 'POST'] )
def perfil(id):

    if request.method == "POST":
        repositorio.remover_usuario(id)
        return redirect(url_for('login'))
    else: 
        usuario = repositorio.retornar_usuario(id)
        return render_template("perfil.html", **usuario)

@app.route("/editar/<int:id>", methods = ['GET', 'POST'] )
def editar(id):

    if request.method == "POST":
        usuario = {}
        usuario['nome'] = request.form["nome"]
        usuario['sobrenome'] = request.form["sobrenome"]
        usuario['email'] = request.form["email"]
        usuario['idade'] = request.form["idade"]
        usuario['cidade'] = request.form["cidade"]
        usuario['senha'] = request.form["senha"]

        if id in repositorio.retornar_usuarios().keys():
            repositorio.atualizar_usuario(id, usuario)
        return redirect(url_for("perfil", id=id))

    else: 
        usuario = repositorio.retornar_usuario(id)
        return render_template("editar.html", **usuario)


@app.route("/usuarios")
def usuarios():
    dicionario = repositorio.retornar_usuarios()
    return render_template("usuarios.html", dados = dicionario)

@app.route("/usuarios/<int:id>")
def usuario_id(id):
    usuario = repositorio.retornar_usuario(id)
    print(usuario)
    dicionario = repositorio.retornar_usuarios()
    return render_template("usuarios.html", user = usuario, dados = dicionario)

@app.route("/header")
def header():
    
    return render_template("header.html")



app.run(debug=True)