from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"


def carregarLivros():
    if not os.path.exists(ARQUIVO):

        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)

        except json.JSONDecodeError:
            return []


def salvarLivros(listaLivros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        json.dump(
            listaLivros,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


@app.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["anoPublicação"]
        categoria = request.form["categoria"]
        quantidade = request.form["quantExemplares"]

        if (not titulo or not autor or not ano or
                not categoria or not quantidade):

            return "Todos os campos são obrigatórios."

        if not ano.isdigit():
            return "O ano deve conter apenas números."

        if not quantidade.isdigit():
            return "A quantidade deve ser um número inteiro."

        if int(quantidade) <= 0:
            return "A quantidade deve ser maior que zero."

        livros = carregarLivros()
        livro = {
            "id": len(livros) + 1,
            "titulo": titulo,
            "autor": autor,
            "anoPublicação": ano,
            "categoria": categoria,
            "quantExemplares": quantidade
        }

        livros.append(livro)

        salvarLivros(livros)

        return redirect(url_for("listar"))
    return render_template("cadastro.html")

@app.route("/livros")
def listar():
    livros = carregarLivros()

    return render_template(
        "livros.html",
        livros=livros
    )

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    livroEncontrado = None

    if request.method == "POST":
        titulo = request.form["titulo"].lower()
        livros = carregarLivros()

        for livro in livros:

            if livro["titulo"].lower() == titulo:

                livroEncontrado = livro
                break

    return render_template(
        "buscar.html",
        livro=livroEncontrado
    )


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    livros = carregarLivros()

    for livro in livros:

        if livro["id"] == id:

            if request.method == "POST":

                livro["titulo"] = request.form["titulo"]
                livro["autor"] = request.form["autor"]
                livro["anoPublicação"] = request.form["anoPublicação"]
                livro["categoria"] = request.form["categoria"]
                livro["quantExemplares"] = request.form["quantExemplares"]

                salvarLivros(livros)

                return redirect(url_for("listar"))

            return render_template(
                "editar.html",
                livro=livro
            )

    return redirect(url_for("listar"))

@app.route("/excluir/<int:id>")
def excluir(id):
    livros = carregarLivros()

    livros = [livro for livro in livros if livro["id"] != id]

    salvarLivros(livros)

    return redirect(url_for("listar"))

if __name__ == "__main__":
    app.run(debug=True)