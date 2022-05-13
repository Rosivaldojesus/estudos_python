import psycopg2

# Função para criar conexão no banco

conn = psycopg2.connect(host='127.0.0.10', database='auladb', user='postgres',  password='admin')
cur = conn.cursor()


# Fetch all rows from table
cur.execute("SELECT * FROM banco;")
dados = cur.fetchall()


# Print all rows
for row in dados:
  print("Data row = (%s, %s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]), str(row[3]) ))