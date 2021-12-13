import requests # Bilioteca para fazer a requisão da API
import time # Biblioteca para calcular o tempo

#Criar um decorador para calcular_tempo

def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f'O tempo para executar o código, foi de {tempo_final - tempo_inicial} segundos')
    return wrapper


@calcular_tempo #Chamando o decorador
def pegar_cotacao_bitcoin():
    url = f'https://www.mercadobitcoin.net/api/BTC/ticker/'
    requisicao = requests.get(url)
    requisicao = requisicao.json()
    print(f" O valor atual do bitcoin é de R$: { requisicao['ticker']['last'] } ")

pegar_cotacao_bitcoin()
