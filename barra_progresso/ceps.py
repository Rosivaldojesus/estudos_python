import requests
from tqdm import tqdm


# Abrir o arquivo que contem as lista de ceps
with open('ceps.txt') as arquivo:
    ceps = arquivo.read()
ceps = ceps.split()

enderecos_de_entrega = []
for cep in tqdm(ceps):
    # Utilizando a API de consulta de ceps
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    requisicao = requests.get(link)
    resposta = requisicao.json()
    # Pegando a cidade
    cidade = resposta['city']
    # Pegando o bairro da cidade
    bairro = resposta['district']

    if cidade == "Rio de Janeiro":
        enderecos_de_entrega.append((bairro))

print(enderecos_de_entrega)






