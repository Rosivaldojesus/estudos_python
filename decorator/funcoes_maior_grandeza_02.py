"""
Retornando funções com outras funções
"""


from random import choice


def faz_me_rir():
    def rir():
        return choice(('kkkk', 'rsrsrs', 'uhuuhuhu'))
    return rir

#  Chamando


rindo = faz_me_rir()
print(rindo())
