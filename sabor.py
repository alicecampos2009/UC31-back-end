from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):
    return render_template(f'{sabor}.html')

if __name__ == '__main__':
    app.run(debug=True) 