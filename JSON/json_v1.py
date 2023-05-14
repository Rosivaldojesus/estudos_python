# Importando o módulo JSON
import json


#Criando um dicionário
print('===========================================================')
dict_rosivaldo = {'nome':'Rosivaldo de Jesus',
                  'linguagem':'Python',
                  'similar': ['C','Moluda-3', 'lisp'],
                  'users': 10000 }

# Percorrendo o dicionário
for k,v in dict_rosivaldo.items():
  print(k,v)
print('===========================================================')
# COnvertendo o dicionário para um objeto json
print(json.dumps(dict_rosivaldo))

print('===========================================================')

# Criando um arquivo JSON
with open('JSON/dados.json', 'w') as arquivo:
  arquivo.write(json.dumps(dict_rosivaldo))
print('===========================================================')

# Leitura de arquivos JSON
with open('JSON/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
    print(dados)
    

print(dados['nome'])
    
 