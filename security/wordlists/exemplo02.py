"""
Wordlists são arquivos contendo uma palavra por linha. São utilizado em ataques de força bruta
como quebra de autenticação, pode ser usada para testar a autenticação e confidencialidade de
um sistema

itertools - Biblioteca 
"""
import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))