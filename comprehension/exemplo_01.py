""" Dobrar os valores da lista"""

lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos = []

#  Resovendo de forma normal
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(nova_lista_precos)


#  Resolvendo por list comprehenson
nova_lista_precos = [preco * 2 for preco in lista_precos]
print(nova_lista_precos)
