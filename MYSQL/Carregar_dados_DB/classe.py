import mysql.connector


class DB:
      

  def dados_DB():
      return mysql.connector.connect(host='localhost',  user='root', passwd='', database='speed')