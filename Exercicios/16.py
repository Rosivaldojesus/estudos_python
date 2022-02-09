"""
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
Inteira.
"""
import math
numero = float(input("Digite um valor qualquer: "))

print(f'A parte inteira de {numero} é igual a {math.trunc(numero)}')