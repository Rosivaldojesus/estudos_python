from tqdm import tqdm
import time

novos_produtos = []

produtos = ['Uva', 'Laranja', 'Manga', 'Goiba', 'Melancia', 'Morango']

for produto in tqdm(produtos):
    novos_produtos.append(produto)
    time.sleep(1)

print(novos_produtos)
