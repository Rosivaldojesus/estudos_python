import requests

requisicao = requests.get("https://projetogetpost-default-rtdb.firebaseio.com/.json")
print(requisicao)
print(requisicao.json())


