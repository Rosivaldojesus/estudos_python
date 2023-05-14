import pandas as pd
import mysql.connector

# Ler a planilha
Sheet_df = pd.read_excel("clientes.xlsx")

for i, DADOS in enumerate(Sheet_df['Doc']):
