from mysql.connector import connect


def conectar_banco_dados():
    conexao = connect(
        host='localhost',
        port='3306',
        user='root',
        passwd=''
    )
    print("Conectado ao Banco de dados")
    return conexao


try:
    conectar_banco_dados()
except:
    print('Ops! Ocorreu um erro na conexão com o DB')
