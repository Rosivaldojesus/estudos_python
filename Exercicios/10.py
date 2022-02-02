"""
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.
"""

valor = int(input("Qual valor você tem: "))
valor_dollar = 5.45

compra = valor/valor_dollar

print(f'Com R$:{valor}, você pode comprar USD: {compra}')
