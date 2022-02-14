import requests


requisicao = requests.delete("https://projetogetpost-default-rtdb.firebaseio.com/-MvuIoHvAxWdV2lJSYZ9/-MvuJ_AItG-Ksqe4Dcy6.json")
print(requisicao)
print(requisicao.json())