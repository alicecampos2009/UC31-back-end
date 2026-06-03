from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def cadastroAlunos():
    return render_template('cadastroAlunos.html')


@app.route('/validacao', methods=['POST'])
def cadastro():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip()
    cpf = request.form.get('cpf', '').strip()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().upper()
    curso = request.form.get('curso', '').strip()
    idade = request.form.get('idade', '').strip()
    senha = request.form.get('senha', '').strip()

    telefone = telefone.replace('(', '')
    telefone = telefone.replace(')', '')
    telefone = telefone.replace(' ', '')
    telefone = telefone.replace('-', '')

    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    if not all([nome, email, telefone, cpf, cidade, estado, curso, idade, senha]):
        return "Preencha todos os campos obrigatórios."

    if len(nome) < 8:
        return "Nome inválido."

    if '@' not in email or '.com' not in email:
        return "E-mail inválido."

    if len(telefone) != 11 or not telefone.isdigit():
        return "Telefone inválido."

    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido."

    if len(cidade) < 3:
        return "Cidade inválida."

    if len(estado) != 2 or not estado.isalpha():
        return "Estado inválido."

    if not curso:
        return "Curso inválido."

    if not idade.isdigit():
        return "Idade inválida."

    idade = int(idade)

    if idade < 16:
        return "Idade inválida."

    if len(senha) < 8:
        return "Senha muito fraca."

    possui_numero = False

    for caractere in senha:
        if caractere.isdigit():
            possui_numero = True

    if not possui_numero:
        return "Senha muito fraca."

    return f"""
    <h1>Cadastro realizado com sucesso!</h1>

    Nome: {nome} <br>
    E-mail: {email} <br>
    Telefone: {telefone} <br>
    CPF: {cpf} <br>
    Cidade: {cidade} <br>
    Estado: {estado} <br>
    Curso: {curso} <br>
    Idade: {idade}
    """


if __name__ == '__main__':
    app.run(debug=True)