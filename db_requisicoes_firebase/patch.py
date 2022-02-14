import requests

informacoes = '{"Nome": "Rosivaldo", "Sobrenome": "Jesus", "idade": "32"}'

requisicao = requests.patch("https://projetogetpost-default-rtdb.firebaseio.com/-MvuIoHvAxWdV2lJSYZ9.json", data=informacoes)
print(requisicao)
print(requisicao.json())