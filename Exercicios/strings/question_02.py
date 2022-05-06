"""
Escreva um programa Python para contar o número de caracteres (frequência de caracteres) em uma sequência.
"""

texto = input('Digite uma frase: ')

def char_frequency(paramentro):
    dicionario = {}
    for n in paramentro:
        keys = dicionario.keys()
        if n in keys:
            dicionario[n] += 1
        else:
            dicionario[n] = 1
    return dicionario
print(char_frequency(texto))


