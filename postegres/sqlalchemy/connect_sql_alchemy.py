from sqlalchemy import create_engine

db_string = "postgresql://postgres:admin@127.0.0.10:5432/auladb"

db = create_engine(db_string)


# Read
result_set = db.execute("SELECT * FROM banco")  
for r in result_set:  
    print(r)

