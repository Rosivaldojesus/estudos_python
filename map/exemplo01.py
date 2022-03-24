# MAP => Aplica uma função em cada item de uma lista

precos = [100, 1500, 1250, 2500]

# Do jeito manual=========================================================
def adicionar_imposto(preco):
    return preco * 1.1

precos_com_impostos = []
for preco in precos:
    precos_com_impostos.append(adicionar_imposto(preco))
print(precos_com_impostos)

print('===============================================================')
print('===============================================================')
# Usando MAO ======================================================================
precos_com_impostos2 = map(adicionar_imposto, precos)

print(list(precos_com_impostos2))