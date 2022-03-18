"""
BIBLIOTECAS- 

- re: Permite Operações com expressões regulares
- json: Fornece operaçao de codificação e decodificação JSON
- urllib.request import urlopen:Funções e classes que ajudam a abrir URLs

http://ipinfo.io/json
"""

import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']


print('Detalhes do IP Externo\n')
print(f'IP: {ip}\nAS: {org}\nCidade: {city}\nPais: {country}\nRegião:{region}' )