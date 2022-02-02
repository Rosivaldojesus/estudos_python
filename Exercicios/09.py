"""
Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

numero = int(input("Digite um número: "))

multiplo = 0

while multiplo < 9:
    multiplo = multiplo + 1
    print(f'{numero} X {multiplo} = { numero * multiplo}')
