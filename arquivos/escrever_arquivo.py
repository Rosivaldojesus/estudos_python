def escrever_arquivo(texo):
    arquivo = open('texto.txt', 'w')
    arquivo.write(texo)
    arquivo.close()

if __name__ == '__main__':
    escrever_arquivo('Primeira linha')
