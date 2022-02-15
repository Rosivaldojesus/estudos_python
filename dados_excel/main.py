#  Instalar( Pandas, openpyxl)
import pandas as pd

#  Abrir os arquivos da base de dados
lista_meses = ['dados.janeiro']

tabela_vendas = pd.read_excel("janeiro.xlsx")

print(tabela_vendas)
#  Para cada arquivo