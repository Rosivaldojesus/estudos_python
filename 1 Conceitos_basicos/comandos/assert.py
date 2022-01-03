"""
Verifica o valor de expressão; se for falso, será disparada uma exceção. Se ocorrer uma exceção e argumento for
especificado, este será utulizado como argumento da exceção. É utilizado na depuração de programas.

------------------------------------------------------------------------------------------------------------------------
#  Exemplo 1: Verifca um número digitado. Se for negativo, será disparada uma exceção
numero = int(input('Digite um número positivo: '))
assert numero > 0

"""
#  Exemplo 2: Verifca um número digitado. Se for negativo, será disparada uma exceção, mas com o uso de argumento

numero = int(input("Digite um número positivo: "))
assert numero > 0, "Por favor, um número positivo."
