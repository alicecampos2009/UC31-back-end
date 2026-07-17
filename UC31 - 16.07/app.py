from flask, import Flask, render_template
import json

@app.route("/")
def produtos():
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        lista_produtos = json.load(arquivo)

    return render_template("produtos.html", produtos=lista_produtos)

app.run(debug=True) 