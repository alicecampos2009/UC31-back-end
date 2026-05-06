# QUESTÃO 01
@app.route('/dados', defaults={"nome": "usuario comum"})

@app.route('/dados/<nome>')
def dados(nome):
    return render_template('saudacao.html', nome=nome)

# QUESTÃO 02
@app.route('/calculo/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return render_template('soma.html', resultado=resultado, n1=n1, n2=n2)

# QUESTÃO 03
@app.route('/idade/<nome>/<int:idade> ')
def verificar_idade(nome, idade):
    if idade >= 18:
        mensagem = f"{nome} é maior de idade"
    else:
        mensagem = f"{nome} é menor de idade"
    
    return render_template('idade.html', mensagem=mensagem)

# QUESTÃO 04
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return render_template('produto.html', nome=nome, preco=preco)