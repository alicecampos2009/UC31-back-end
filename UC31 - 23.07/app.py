from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "123456"

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "Marina" and senha == "1234":
            session["usuario_nome"] = usuario
            return redirect(url_for("painel"))

        flash("Usuário ou senha incorretos!")

    return render_template("login.html")


@app.route("/painel")
def painel():

    if "usuario_nome" not in session:
        flash("Faça login primeiro!")
        return redirect(url_for("login"))

    return render_template(
        "painel.html",
        nome=session["usuario_nome"]
    )


@app.route("/cantinho")
def cantinho():

    if "usuario_nome" not in session:
        flash("Faça login para acessar o cantinho secreto!")
        return redirect(url_for("login"))

    nome = session.get("usuario_nome")

    return render_template(
        "cantinho.html",
        nome=nome,
        cor="Azul",
        linguagem="Python",
        frase="Tudo é difícil antes de se tornar fácil."
    )


@app.route("/logout")
def logout():

    session.clear()
    flash("Logout realizado!")

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)