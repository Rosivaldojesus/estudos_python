"""
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
graus Fahrenheit.
"""

celsius = int(input("Qual a temperatura em celsius: "))

fahrenheit = (celsius * (9/5)) + 32

print(f'{celsius}ºC é igual a {fahrenheit}ºF')
