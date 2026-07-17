from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

nome_usuario = ""
senha_hash = ""
usuario_logado = False

@app.route("/", methods=["GET", "POST"])
def cadastro():
    global nome_usuario, senha_hash

    if request.method == "POST":
        nome_usuario = request.form["nome"]
        senha_hash = generate_password_hash(request.form["senha"])
        return redirect(url_for("login"))

    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    global usuario_logado

    erro = ""

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]

        if nome == nome_usuario and check_password_hash(senha_hash, senha):
            usuario_logado = True
            return redirect(url_for("inicio"))
        else:
            erro = "Usuário ou senha inválidos."

    return render_template("login.html", erro=erro)

@app.route("/inicio")
def inicio():
    if not usuario_logado:
        return redirect(url_for("login"))

    return render_template("inicio.html", nome=nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)