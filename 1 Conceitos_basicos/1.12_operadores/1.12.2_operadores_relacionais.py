"""
Estabelecem uma realção entre dois operandos, que normalmente, são uma variável e uma constante ou duas variáveis,
criando uma expressão relacional que produz um resultado lógico verdadeiro(True) ou falso(False).

Tabela. Operadores relacionais
Operador	Significados
> - (Maior que)
< - (Menor que)
>= - (Maior ou igual a)
<= - (Menor ou igual a)
!= - (Não igual a)
== - (Igual a)

"""
print('Exemplo 1: Operador <')
valor1 = 20
valor2 = 30
print(valor1 < valor2)
print('--------------------------------------------------------')

#---------------------------------------
print('Exemplo 2: Operador != em um comando if')
valor1 = 20
valor2 = 30
if valor1 != valor2:
    print("Diferentes")
else:
    print('Iguais!!!')