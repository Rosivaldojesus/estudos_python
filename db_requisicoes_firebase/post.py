"""
É preciso passar os parâmetros
"""

import requests

informacoes = '{"Nome": "Rosivaldo"}'

requisicao = requests.post("https://projetogetpost-default-rtdb.firebaseio.com/.json", data=informacoes)
print(requisicao)
print(requisicao.json())