import requests

dollar = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print('Valor atual do dollar é U$D: ' + dollar.json()['USDBRL']['bid'])