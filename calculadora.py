from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('projetos.html', resultado=None)

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']

        if operacao == 'somar':
            resultado = num1 + num2
        elif operacao == 'subtrair':
            resultado = num1 - num2
        elif operacao == 'multiplicar':
            resultado = num1 * num2
        elif operacao == 'dividir':
            resultado = num1 / num2 if num2 != 0 else 'Erro: divisão por zero'
        else:
            resultado = 'Operação inválida'
    except Exception as e:
        resultado = f'Erro: {e}'
    
    return render_template('projetos.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
