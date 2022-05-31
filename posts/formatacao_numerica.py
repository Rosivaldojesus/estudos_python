# Ponto separador de decimal

faturamento = 1500
custo = 500
lucro = faturamento - custo
print(f'O lucro foi de R$: {lucro}')
print(f'O lucro foi de R$: {lucro:,.2f}')


print('------------------------------------------')


margem = lucro / faturamento
print(f'A margem foi de {margem}')
print(f'A margem foi de {margem:.1%}')


print('------------------------------------------')
# Colocando em formaro de moeda brsileia

texto_lucro = f'R$: {lucro:_.2f}' 
texto_lucro = texto_lucro.replace('.', ',').replace('_', '.')
print(f'O lucro foi de {texto_lucro}')