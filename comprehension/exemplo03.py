"""
List comprehension
lista_num = [ x**2 for x in range(100)]
lista_par = [x for x in lista_num if x % 2 == 0]
---------------------------------------------------------------------------------------------------
"""
lista_numeros = []
lista_pares = []

for x in range(100):
    lista_numeros.append(x**2)

for par in lista_numeros:
    if par % 2 == 0:
        lista_pares.append(par)

print(lista_pares)
