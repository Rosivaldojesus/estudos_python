"""
 - *args: (Argumentos sem palavra-chave)

 A sintaxe especial *args nas definições de função em python é usada para passar um número variável de argumentos para
 uma função. É usada para passar uma lista de argumentos de comprimento variável e sem palvras-chave.

    - A sintaxe é usar um o símbolo * para obter um números variável de argumentos: poe convenção, é frequentemente
    usado com a palavras args.
    - O que *args permite que você faça é aceitar mais argumentos do que o número de argumentos formais que você
    definiu anteriormente. Com o *args, qualquer número de argumentos extras pode ser adicionado aos seus parâmetros
    formais atuais (incluindo nenhum argumento extra).
    - Por exemplo: queremos fazer uma função de multiplicação que recebe qualuer número de argumentos e seja capaz de
    multiplicá-los todos juntos. Isso pode ser feito usando o *args
    - Usando *, a variável que associamos com * torna-se um significado iterável, você pode fazer coisas como interar
    sobre ela, executar algumas funções de ordem superior, como mapear e filtar, etc.
"""

""" O *args é usado em uma função para fazeê-la receber uma lisa de argumentos sem tamanho definido sem palavra-chave
(keyword)"""


#  Exemplo 01


def minha_funcao_1(*args):
    for arg in args:
        print(arg)


minha_funcao_1('Olá', 'Bem-vindo', 'para', 'terra')
print("-------------------------------------------------------------------------------")


#  Exemplo 02
def minha_funcao_2(argumento1, *args):
    print("Primeiro argumento: ", argumento1)
    for arg in args:
        print("Próximo argumento por meio de *args: ", arg)


minha_funcao_2('Olá', 'Bem-vindo', 'para', 'terra')


#  Exemplo 03
def funcao(*args):
    for arg in args:
        print('Argumento de *args: {args}')
funcao('arg1', 'agr2', 'arg3', 'arg4', 'arh5')

