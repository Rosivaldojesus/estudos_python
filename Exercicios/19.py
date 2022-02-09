"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
import random

aluno1 = input("Digite um nome: ")
aluno2 = input("Digite um nome: ")
aluno3 = input("Digite um nome: ")
aluno4 = input("Digite um nome: ")
aluno5 = input("Digite um nome: ")

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

print(f'Esses são os alunos: {lista_alunos}')
print(f'O aluno escolhido foi {random.choice(lista_alunos)}')