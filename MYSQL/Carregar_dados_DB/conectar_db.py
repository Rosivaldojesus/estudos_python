import mysql.connector
import pandas as pd
from classe import DB

# Informações do banco de dados
con = DB.dados_DB()

# Exibindo que está conectado a DB
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado DB de versão: ", db_info)
    
# Exibindo o nome do DB
cursor = con.cursor()
cursor.execute("select database();")
linha = cursor.fetchone()
print("Banco de dados: ", linha)

# Criando tabela no DB
Sheet_df = pd.read_excel("MYSQL\Carregar_dados_DB\clientes.xlsx")
print(Sheet_df.head())

# for index, row in Sheet_df.iterrows():
#     sql = "INSERT INTO contatos (nome, cpf) VALUES (%s, %s)"
#     val = (row['nome'], row['cpf'])
#     cursor.execute(sql, val)
#     con.commit()
    


# Fechando conexão com o DB
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada!")