'''
Split: Dividi uma string
'''

string = '''
 alerta vermelho do Inmet é para o grande risco de alagamentos e transbordamentos de rios,
  deslizamentos de encostas em cidades com áreas de risco. Há alerta laranja,
   de perigo, para riscos de tempestades e quedas de árvores. E alerta e risco amarelo para o risco de raios.
'''

lista_1 = string.split(' ') # Separado por espaço
lista_2 = string.split(',') # Separado por vírgula


# Mostar as palavras e quantas vezes ele apareceu
#for valor in lista_1:
    #print(f'A palavra <<{valor}>> apareceu: {lista_1.count(valor)}')

# Quantas vezes uma determinada apareceu na frase
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é <<{palavra}>> ({contagem}x)')