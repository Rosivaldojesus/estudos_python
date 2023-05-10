import psycopg2

# Função para criar conexão no banco
conn = psycopg2.connect(
  
  database='derns967m7j06t',
  user='fdyyovzteqpivo',
  host='ec2-18-215-41-121.compute-1.amazonaws.com',
  password='a689c697671cfde6d8af3f7a86b58973951ce508116dd6812933083183ca7d09',
  port='5432'
  
)
cursor = conn.cursor()

# Fetch all rows from table

# consulta_sql = '''SELECT * FROM\
#   components_bairros;'''

consulta_sql = '''SELECT * FROM components_bairros;'''


cursor.execute(consulta_sql)
dados = cursor.fetchall()

# Print all rows
for row in dados:
  print("Data row = (%s, %s)" %(str(row[0]), str(row[1])))