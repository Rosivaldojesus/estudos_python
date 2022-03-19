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



palavra = ''
contagem = 0
for valor in lista_2:
    print(valor.strip())
