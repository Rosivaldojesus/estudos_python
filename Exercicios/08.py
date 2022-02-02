"""
Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
metragem = int(input("Qual a metragem: "))

centimetros = metragem * 100
milimetros = metragem * 1000

print(f'{metragem}m tem {centimetros}cm')
print(f'{metragem}m tem {milimetros}mm')
