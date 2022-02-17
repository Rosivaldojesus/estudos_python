import re

string = "Essa é uma frase com espaços demais no final.           "
re.sub("\s+$", "", string)

print(string)