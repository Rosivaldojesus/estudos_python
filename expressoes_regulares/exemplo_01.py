from cgitb import text
import re

texto = "Algoritmos e Programação de Computadores"
resultado = re.search(r'(\w*)ama(\w*)', texto)
print(type(resultado))
print(resultado.group())
print(resultado.span())
print(re.search(r'^\w*', texto))
print(re.search(r'^\w*$', texto))