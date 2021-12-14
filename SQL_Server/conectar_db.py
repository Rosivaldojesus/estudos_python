# Instalar: pyodbc

import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-HVTNLUB\SQLEXPRESS;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)

print('Conexão bem sucedida!!!')



cursor = conexao.cursor()
cursor.execute('SELECT * FROM Vendas')
for i in cursor:
    print(i)