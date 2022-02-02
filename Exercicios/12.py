"""
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco_atual = int(input("Qual o valor do produto: "))
valor_desconto = ((preco_atual / 100) * 5)
novo_valor = preco_atual - valor_desconto
print(f'O produto de R$: {preco_atual} com 5% de desconto custará R$: {novo_valor}')
