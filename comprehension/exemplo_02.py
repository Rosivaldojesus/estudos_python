""" Todos os produtos que custam acima de 1000 dolares, imposto de 50% sobre o valor total"""

lista_produtos = [500, 1500, 2000, 100, 25]
imposto = []

#  Resolvendo de forma padrao
for preco in lista_produtos:
    if preco > 1000:
        imposto.append(preco * 0.5)
print(imposto)

#  Resolvendo usando list comprehension
imposto = [preco * 0.5 for preco in lista_produtos if preco > 1000]
print(imposto)