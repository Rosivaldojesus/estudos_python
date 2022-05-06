"""
Escreva um programa Python para calcular o comprimento de uma sequência.
"""

texto = input("Digite uma frase: ")

def string_lenght(parametro):
    contagem = 0
    for caractere in parametro:
        contagem += 1
    return contagem

print(string_lenght(texto))
    
