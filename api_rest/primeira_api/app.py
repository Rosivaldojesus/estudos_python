from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def pessoa():
    return jsonify(
        {'id': 1, 'nome': 'Rosivaldo', 'profissao': 'Desenvolvedor' },    
    )

if __name__=='__main__':
    app.run(debug=True)
