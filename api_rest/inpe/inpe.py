from numpy import fromstring
import requests, os, sys

from lxml import html


def listar_meses(url):
    page = requests.get(url);
    if page.status_code != 200:
        return
    tree = html fromstring( page.text );
    

def listar_anos():
    url = 'http://ftp.cptec.inpe.br/modelos/tempo/BAM/TQ0666L064/recortes/grh/json/';
    for ano in [2019,2020,2021,2022]:
        listar_meses(url + str(ano) + '/' );