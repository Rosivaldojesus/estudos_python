"""
Um web scraping é uma ferramenta de coleta de dados web, uma forma de mineração que permite a
extração de dados de sites da web convertendo-os em informação estruturada para posterior análise.

BeautifulSoup - É uma biblioteca de extração de dados de arquivos e xml

requests - Permite que você envie solicitações HTTP em Python.
"""

from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.globo.com/").content
# O objeto site está recebendo o conteúdo da requisição http do site...

soup = BeautifulSoup(site, 'html.parser')
# O objeto soup baixando o site html

print(soup.prettify())
# Transforma html em strinh e o print exibi o html

#informacao = soup.find('span', class_="")
#print(informacao.string)