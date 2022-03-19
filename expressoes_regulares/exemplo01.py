import re

# findall search sub
# compile

string = 'Este é um teste de expressoes teste regulares'

# Procura a palavra "teste" dentro da variável string
print(re.search(r'teste', string)) # Dar match

# Exibi uma lista com as palavra "teste", localizada
print(re.findall(r'teste', string)) # Lista

# Localiza e substitui a palavra por outra
print(re.sub(r'teste', 'ABC', string)) # Substitui

# Utilizando o compile
print('---------------------------------------------')

regex = re.compile(r'teste')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub('DEF', string))