"""
Assetions (Afirmações/Checagens/Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não. Se a expressão for verdadeira,
retorna None e caso seja falsa levanta um erro do tipo AssertionError.

OBS.: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizado.

- OBS.: A palavara 'assert' pode ser utilizada em qualquer função ou código nosso.. não precisa ser
exclusivamnete nos testes.
"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b
resultado = soma_numeros_positivos(6, 8) # 14
#resultado = soma_numeros_positivos(6, -8) # AssertionError
print(resultado)

