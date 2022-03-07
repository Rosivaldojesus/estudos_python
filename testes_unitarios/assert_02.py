def comer_fast_food(comida):
    assert comida in [
        'pizza', 'sorvete', 'doces', 'batata frita', 'cachorro quente'
    ], 'A comida precisa ser fast food.'
    return f'Eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))