"""
- Instalar: MYSQL Connector
"""

try:
    from mysql import connector
except ModuleNotFoundError:
    print("MYSQL Conncetor não instalado!")
else:
    print('MYSQL Connector instalado e pronto!')