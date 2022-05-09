import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


print(dados) 