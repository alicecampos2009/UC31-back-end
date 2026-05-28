from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    estado = request.form['estado']
    formacao = request.form['formacao']
    modalidade = request.form.getlist('modalidades')

    return "{} e {} e {} e {} e {}".format(nome, email, estado, formacao, modalidade)

if __name__=='__main__':
    app.run(debug=True)