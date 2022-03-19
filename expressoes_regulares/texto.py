import re

texto = '''

Entre a noite deste sábado e o domingo (20), a frente desacelera seu deslocamento
e promove acumulados de chuva significativos no leste do estado, os quais devem 
superar os 100 mm em 24h em diversas localidades, sendo que em áreas do litoral 
e de relevo mais acentuado (cercanias da Serra do Mar) os volumes podem ultrapassar
os 200 mm no período.
'''

# Pega apenas as letras minusculas
# print(re.findall(r'[a-z]+', texto))

# Pega apenas as letras minusculas e maiusculas
# print(re.findall(r'[a-zA-Z]+', texto))

# Pega apenas as letras minusculas e maiusculas e números
#print(re.findall(r'[a-zA-Z0-9]+', texto))


# Pega apenas as letras minusculas e maiusculas e números e letras acentuadas
#print(re.findall(r'[a-zA-Z0-9Á-ú]+', texto))

# Fazendo uma negação
#print(re.findall(r'[^a-zA-Z0-9Á-ú]+', texto))
