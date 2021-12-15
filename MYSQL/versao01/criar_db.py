from MYSQL.versao01.conexao_db import conectar_banco_dados

# A variável conexao receber a função conectar_banco_dados(), do arquivo conexao_db, que está dentro do mesmo pacote
conexao = conectar_banco_dados()


cursor = conexao.cursor()
#  CREATE DATABASE IF NO EXISTS
cursor.execute('CREATE DATABASE agenda')
