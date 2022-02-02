"""
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele.
"""

infor = input("Digite uma informação qualquer: ")

print("O tipo de dado é: ", type(infor))

print("É minuscula: ", infor.islower())
print("É maíuscula: ", infor.isupper())
