"""
Em python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions ou também Inner Functios
(Funções Internas)

Abaixo um exemplo
"""


from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma daqui', 'Gosto muito de você'))
    return humor() + ' ' + pessoa


#  Chamando a função


print(cumprimento('Ana'))
