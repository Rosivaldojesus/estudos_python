"""
Escreva um programa Python para selecionar um elemento aleatório de uma lista, conjunto,
dicionário (valor) e um arquivo de um diretório.

Use random.choice
"""
import random
import os

# Selecione um elemento aleatório de uma lista

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(elements))

# Selecione um elemento aleatório de um conjunto
elements = ([1, 2, 3, 4, 5, 6, 7, 8])
print(random.choice(tuple(elements)))

# Selecione um valor aleatório de um dicionário
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "d": 6}
key = random.choice(list(dictionary))
print(dictionary[key])

# Selecione um arquivo aleatório de um diretório
print(random.choice(os.listdir("/")))
