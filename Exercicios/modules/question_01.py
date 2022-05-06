"""
Escreva um programa Python para gerar um hexacampeão de cores aleatória, uma sequência alfabética
 aleatória, valor aleatório entre dois inteiros (inclusive) e um múltiplo aleatório de 7 entre 0 e 70.
  Use random.randint()
"""
import random
import string


# Gera uma cor hexadecimal aleatório:
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))

# Gerar uma string alfabética aleatória:
max_lenght = 255
s = ""
for i in range(random.randint(1, max_lenght)):
    s += random.choice(string.ascii_letters)
print(s)

# Gere um valor aleatório entre dois números inteiros, inclusive:
print(random.randint(0, 21))
print(random.randint(-8, 33))
print(random.randint(3, 3))

# Gere um múltiplo aleatório de 7 entre 0 e 70:
print(random.randint(0, 10) * 7)