from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("indexTechFuture.html")

@app.route("/cursos")
def inicio():
    return render_template("cursoTechFuture.html")

@app.route("/professores")
def inicio():
    return render_template("professoresTechFuture.html")

@app.route("/contato")
def inicio():
    return render_template("contatoTechFuture.html")

if __name__ == "__main__":
    app.run(debug=True) 