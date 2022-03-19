# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | = OU
# . = Qualquer caractere
# [] conjunto de caracteres


import re

texto = """
Agora que nós vimos algumas Expressão regulares simples, como nós realmente as usamos em Python? O módulo re fornece
 uma interface para o mecanismo de expressão regular, permitindo compilar REs em objetos e, em seguida, executar 
 comparações com eles.
"""

print(re.findall(r'módulo|objetos|eles', texto)) # |
print(re.findall(r'real....e', texto)) # . 
print(re.findall(r'[eE]xpressão', texto)) # []

# Determinando um range de letra dentro do "[]"
print(re.findall(r'[a-zA-Z0-9]xpressão', texto)) # [] Range

# Ignora maiuscula de minuscula
print(re.findall(r'expressão', texto, flags=re.IGNORECASE)) # [] Range
