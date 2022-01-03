"""
**kwargs (Argumentos de palavra-chave)

 - A sintaxe especial **kwargs nas definições de função em python é usada para passar uma lista de argumentos de
 comprimento variável com palavras-chave. Usamos o nome kwargs com a estrela dupla. A razão é porque a estrela dulpla
 permite passar por argumentos de palvras-vhave ( e qulauer número deles).

  - Um argumento de palavra-chave é onde você fornece um nome para a variável ao passá-la para a função.
  - Pode-se pensar nos kwargs como um dicionário que mapeia cada palavra-chave para o valor que passamos junto com ela.
  É por isso que, quando iteramos sobre os kwargs, não parece haver nenhuma ordem que foram impressoa.

"""

""" **kwargs nos permite nomear os argumentos e passar, para as funções parâmetros com nomes"""


#  Exemplo de uso de **kwargs
def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} == {value}')

minha_funcao(Primeiro='Geeks', Meio='for', ultimo='Geeks')


#  Exemplo 2
def funcao(**kwargs):
    print(f'**kwargs: { kwargs}')

    for kwarg in kwargs.values():
        print(f'Argumento de **kwargs: {kwarg}')

funcao(a='kwarg1', b='kwarg2', c='kwarg3')