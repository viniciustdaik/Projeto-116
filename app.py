# importando os módulos da biblioteca flask
from flask import Flask, render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'


@app.route("/")
def home():

    nome = "Vinícius"  # escreva seu nome
    idade = "14"  # escreva sua idade
    img = "/static/eu.jpg"
    relation = "Eu"

    return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# defina a rota para a página do pai


@app.route("/pai")
def pai():

    nome = "Marcos"  # escreva seu nome
    idade = "40"  # escreva sua idade
    img = "/static/pai.jpg"
    relation = "Pai"

    return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# defina a rota para a página da mãe


@app.route("/mae")
def mae():

    nome = "Vania"  # escreva seu nome
    idade = "50"  # escreva sua idade
    img = "/static/mae.jpeg"
    relation = "Mãe"

    return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# defina a rota para a página do amigo


@app.route("/irmao")
def irmao():

    nome = "Davi"  # escreva seu nome
    idade = "8"  # escreva sua idade
    img = "/static/irmao.jpg"
    relation = "Irmão"

    return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# adicione outras rotas, se você quiser


@app.route("/vo")
def vo():

    nome = "Veni"  # escreva seu nome
    idade = "79"  # escreva sua idade
    img = "/static/vo.jpg"
    relation = "Vó"

    return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)


# execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)
