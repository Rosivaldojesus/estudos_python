from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

temperatura = soup.find("span", class_="-gray-light")
print(temperatura.string)




