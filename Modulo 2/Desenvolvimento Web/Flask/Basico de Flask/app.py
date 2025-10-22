#importando "partes" do Flask
from flask import Flask, render_template,request

#criando app e dizendo que ele está nesse arquivo com nome dele

app = Flask(__name__)

#criando rotas

# / Significa o local onde o site já vai de cara

@app.route('/')
def olha_mundo():
    return "Ola mundo, Leozzão"

# Aqui vamos criar uma nova rota, dessa vez vai ser a /contato

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/hobbies')
def hobbie():
    return render_template('hobbies.html')

# -------------------------------------------------------

# Sua vez! crie uma nova rota dessa vez /hobbies, lá coloque algo que você goste de fazer, exemplo: Jogar bola

# lembre-se de criar um template chamado /hobbies.html

# executando o arquivo
if __name__ == '__main__':
    app.run(debug=True)