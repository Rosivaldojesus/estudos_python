"""
É uma ferramenta usada para encontrar, ler e indexar págins de um site. 
É como um robô que captura informações de cada um dos links que encontra pela frente,
cadastra e compreende o que é mais relevante.

Muito utilizado em levantamento de informações em um processo de Pentest

BIBLIOTECAS:
 
- BeattifulSoup: Serve para extraçãi de dados de arquivos html e xml
- Operator: Exporta um conjunto de funções eficientes correspondente aos
 operadores intrínsecos do python como: + = * / not and
- collections: Ajudar a preeencher e manupular as estruturas de dados
"""
import operator
from distutils.command.clean import clean
from lib2to3.pygram import Symbols
from pyparsing import Word
import requests
from bs4 import BeautifulSoup

from collections import Counter

import soupsieve

def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    # text in given web-page is stored under
    # the <div> tags with <entry-content>
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\:;"<>?/.,'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("% s: % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/")
