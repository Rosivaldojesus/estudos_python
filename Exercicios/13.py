"""
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15%
de aumento.
"""

salario = int(input("Qual o valor do salário R$: "))
valor_aumento = ((salario /100) * 15)
novo_salario = salario + valor_aumento

print(f'Valor atual do salário R$: {salario}, com aumento de 15% ficará R$: {novo_salario}')
