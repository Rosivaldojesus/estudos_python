def duplicar(valores):
    """ Duplica os valores em uma lista

    :param valores:
    :return:
    >>> duplicar([1,2,3,4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    """

    return [2 * elemento for elemento in valores]