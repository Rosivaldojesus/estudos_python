# Meta caracteres: ^ $
# ^ -> começa com
# $ -> termina com
# [^a-z] -> negação

import re

cpf = '147.852.963-12'
print(re.findall(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', cpf))

# Fazendo um a negação
print(re.findall(r'[^a-z]+', cpf))

