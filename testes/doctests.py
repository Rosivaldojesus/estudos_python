"""
Doctests

Doctests são testes que colocamos na dicstrings das funções/métodos Python.

"""

def soma(a, b):
    """
    Soma os números a e b
    >>> soma(9, 3)
    12
    """
    return a + b

print(soma(9, 3))