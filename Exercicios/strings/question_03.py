"""
Escreva um programa Python para obter uma sequência feita dos primeiros 2 e os últimos
2 chars de uma determinada sequência. Se o comprimento da corda for inferior a 2, retorne
em vez da sequência vazia.
"""

def string_both_ends(paramentro):
    if len(paramentro) < 2:
        return ''
    return paramentro[0:2] + paramentro[-2:]

print(string_both_ends('Desenvolvedor'))
print(string_both_ends('De'))
print(string_both_ends('D'))