"""
Escreva um programa Python para converter objetos Python em strings JSON. Imprima todos os valores.
"""
import json
dicionario_python = {"Nome": "Joana", "Idade": "32", "Profissao": "Desenvolvedor"}
lista_python = ["Vermelho", "Amarelo", "Azul"]
string_python = "Arquivos json Python"
inteiro_python = (12345)
float_python = (212.32)
none_python = (None)

dicionario_python = json.dumps(dicionario_python)
lista_python = json.dumps(lista_python)
string_python = json.dumps(string_python)
inteiro_python = json.dumps(inteiro_python)
float_python = json.dumps(float_python)
none_python = json.dumps(none_python)

print("Dicionário python: ", dicionario_python)
print("Lista python: ", lista_python)
print("String python: ", string_python)
print("Inteiro python: ", inteiro_python)
print("Float python: ", float_python)
print("None python: ", none_python)