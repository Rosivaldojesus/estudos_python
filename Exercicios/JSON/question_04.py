"""
Escreva um programa Python para converter objeto de dicionário Python (tipo por chave) em dados JSON. Imprima os
 membros do objeto com o nível 4 do travessão.
"""
import json

json_string = {'4': 4, '6': 7, '1': 3, '2': 8}

# Imprimindo as strings de forma original
print(json_string)
print('------------------------------')
print(json.dumps(json_string, sort_keys=True, indent=2))