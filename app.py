# importando os módulos da biblioteca flask
from flask import Flask, render_template
import time

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'

myInfo = {"nome": "Vinícius",
          "idade": "14",
          "img": "/static/eu.jpg",
          "relation": "Eu",
          "birthday": "17/04/2008",
          }


def person(information):
    print(information["birthday"])
    return render_template('index.html',
                           nome=information["nome"],
                           idade=information["idade"],
                           img=information["img"],
                           relation=information["relation"],
                           birthday=information["birthday"])


@app.route("/")
@app.route("/eu")
@app.route("/vini")
@app.route("/vinicius")
@app.route("/vinícius")
def home():
    return person(myInfo)

    # nome = "Vinícius"  # escreva seu nome
    # idade = "14"  # escreva sua idade
    # img = "/static/eu.jpg"
    # relation = "Eu"

    # return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# defina a rota para a página do pai


@app.route("/pai")
@app.route("/marcos")
def pai():
    return person({
        "nome": "Marcos",
        "idade": "40",
        "img": "/static/pai.jpg",
        "relation": "Pai",
        "birthday": "",
    })

    # nome = "Marcos"  # escreva seu nome
    # idade = "40"  # escreva sua idade
    # img = "/static/pai.jpg"
    # relation = "Pai"

    # return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# defina a rota para a página da mãe


@app.route("/mae")
@app.route("/vania")
def mae():
    return person({
        "nome": "Vania",
        "idade": "50",
        "img": "/static/mae.jpeg",
        "relation": "Mãe",
        "birthday": "",
    })

    # nome = "Vania"  # escreva seu nome
    # idade = "50"  # escreva sua idade
    # img = "/static/mae.jpeg"
    # relation = "Mãe"

    # return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# defina a rota para a página do amigo


@app.route("/irmao")
@app.route("/davi")
def irmao():
    return person({
        "nome": "Davi",
        "idade": "8",
        "img": "/static/irmao.jpg",
        "relation": "Irmão",
        "birthday": "",
    })

    # nome = "Davi"  # escreva seu nome
    # idade = "8"  # escreva sua idade
    # img = "/static/irmao.jpg"
    # relation = "Irmão"

    # return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)

# adicione outras rotas, se você quiser


@app.route("/vo")
@app.route("/veni")
def vo():
    return person({
        "nome": "Veni",
        "idade": "79",
        "img": "/static/vo.jpg",
        "relation": "Vó",
        "birthday": "",
    })

    # nome = "Veni"  # escreva seu nome
    # idade = "79"  # escreva sua idade
    # img = "/static/vo.jpg"
    # relation = "Vó"
    # birthday = ""

    # return render_template('index.html', nome=nome, idade=idade, img=img, relation=relation)


# execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)
