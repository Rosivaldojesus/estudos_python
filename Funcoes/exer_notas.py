def media(valores):
    media = sum(valores) / len(valores)
    return media


notas = {
    'Rosivaldo': [9, 10, 8, 9], 
    'Fernanda': [9, 7, 6, 9], 
    'Letícia': [8, 9, 7, 10], 
}

for aluno, notas_aluno in notas.items():
    #media = sum(notas_aluno) / len(notas_aluno)
    print(f'{aluno} teve {media(notas_aluno)}')