"""
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

largura = int(input("Digite a largura em metros: "))
altura = int(input("Digite a altura em metros: "))

area = largura * altura
quantidade_tinta = area / 2

print(f'A largura total é de {area}, metros')
print(f'Será necessário {quantidade_tinta} litros de tinta')