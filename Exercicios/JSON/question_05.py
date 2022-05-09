"""
Escreva um programa Python para converter dados codificados JSON em objetos Python.
"""

import json


dicionario_json = '{"Nome": "Rosivaldo", "Idade": "32", "Profissao": "Desenvolvedor"}'
lista_json = '["Vermelho", "Amarelo", "Verde"]'
string_json = '"Json em Python"'
inteiro_json = '1234'
float_json = '23.43'

dicionario_python = json.loads(dicionario_json)
lista_python = json.loads(lista_json)
string_python = json.loads(string_json)
inteiro_python = json.loads(inteiro_json)
float_python = json.loads(float_json)

print("Dicionário Python: ", dicionario_python)
print("Lista Python: ", lista_python)
print("String Python: ", string_python)
print("Inteiro Python: ", inteiro_python)
print("Float Python: ", float_python)


