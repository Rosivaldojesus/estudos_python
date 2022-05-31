import re

# findall search sub
# compile

string = 'Este é um teste de expressões regulares.'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste','avaliação', string, count=1))

print('----------------------------------')

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABC', string))