import re

texto = "Algoritmos e Programação de Computadores"
resultado = re.findall(r'\w+', texto)
print(resultado)

print('----------------------')

telefone = "(019) 91234-5678"
resultado = re.findall(r'[0-9]+', telefone)
print(resultado)