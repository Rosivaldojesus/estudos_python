"""
Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
import math
numero = int(input("Digite um valor númerico: "))

dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero)

print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'Raiz quadrada: {raiz}')
