"""
Escreva um programa Python para converter objeto Python em dados JSON.
"""
import json

objeto_python = {
    "Nome": "Joao",
    "Idade": "32",
    "Profissao": "Desenvolvedor"
}

# verificando o tipo de dados
print(type(objeto_python))

# Convertendo para JSON.
dados_json = json.dumps(objeto_python)

# Resultado em JSON
print(dados_json)