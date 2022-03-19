"""
Funções - def em Python
"""

def funcao(msg='Olá', nome='Usuário'):
    msg = msg.replace('o', 'u')
    nome = nome.replace('o', '3')
    print(msg, nome)

# Exemplo 01
funcao(msg='Olá, tudo bem. Estou aqui', nome='Terra')

# Exemplo 02
funcao('Olá, tudo bem. Estou aqui', 'Rosivaldo')