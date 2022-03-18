
from crypt import methods
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'id': 1, 'nome': 'Rosivaldo', 'habilidade': ['Python', 'Flask']},
    {'id': 2, 'nome': 'Santos', 'habilidade': ['Python', 'Django']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            desenvolvedor = desenvolvedores[id]
            print(desenvolvedor)
            return jsonify(desenvolvedor)
        except IndexError:
            response = {'Status': 'Registro não existe!'}
            return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'Registro excluido com sucesso.'})

# Lista de todos os desenvolvedores 
@app.route('/lista_desenvolvedores', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = request.data
        desenvolvedores.append(dados)
        return jsonify({'status': 'Resgistro adicionado com sucesso.'})


if __name__=="__main__":
    app.run(debug=True)
