# . ^ $ * + ? { } [ ] \ | ( )
# | = OU
# . = Qualquer caractere
import re

texto = """
Agora que nós vimos algumas expressões regulares simples, como nós realmente as usamos em Python? O módulo re fornece
 uma interface para o mecanismo de expressão regular, permitindo compilar REs em objetos e, em seguida, executar 
 comparações com eles.
"""

print(re.findall(r'módulo|objetos', texto))