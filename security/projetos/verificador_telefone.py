"""
BIBLIOTECAS
- phonenumbers: Fornece vários recursos, como informações básicas de um número de telefone,
validação de um números de telefone
"""
import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no seguinte formato +5511988776655: ')
phone_number = phonenumbers.parse(phone)
print(geocoder.description_for_number(phone_number, 'pt'))