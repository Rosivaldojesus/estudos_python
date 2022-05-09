"""
Escreva um programa Python para converter dados JSON em objeto Python
"""
import json
objeto_json = '{"Nome": "João", "Idade":"32", "Profissao": "Desenvolvedor"}'

objeto_python = json.loads(objeto_json)

print("\nJSON data: ")

print(objeto_python)

print("\nNome: ", objeto_python["Nome"])
print("Idade: ", objeto_python["Idade"])
print("Profissão: ", objeto_python["Profissao"])