class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == ' + ':
            print('Aumentar o Canal')
        elif botao == ' - ':
            print('Diminuir o Canal')


controle_remoto = ControleRemoto('Preto', '10cm', '4cm', '20cm')
print(controle_remoto.cor)
controle_remoto.passar_canal(' - ')
