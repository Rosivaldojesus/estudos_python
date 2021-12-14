"""
Inner Functions

"""


from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'kkkkkkkkk', 'rsrsrsrsrsrsrs'))
        return f'{risada} {pessoa}'
    return dando_risada


#  Chamando a função


rindo = faz_me_rir_novamente('Joana')

print(rindo())
print(rindo())
print(rindo())
