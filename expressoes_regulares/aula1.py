import re

# findall, search, sub, compile

string = 'Este é um teste de expressões Teste regulares.'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string))

# Utilizando o compile
print('---------------------------------------------')

regex = re.compile(r'teste')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub('DEF', string))