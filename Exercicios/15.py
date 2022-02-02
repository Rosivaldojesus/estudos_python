"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado.
"""

km_percorridos = int(input("Andou quantos quilômetros: "))
quantidade_dias = int(input("Foram quantos dias de aluguel: "))

valor_km_percorridos = km_percorridos * 0.15
valor_diarias = quantidade_dias * 60
total_pagar = valor_km_percorridos + valor_diarias

print(f'valor pelo quilômetros km: {valor_km_percorridos}')
print(f'Valor das {quantidade_dias} diárias é igual a R$: {valor_diarias}')
print(f'Custo final do aluguel é R$: {total_pagar}')
