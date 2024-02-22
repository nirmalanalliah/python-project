import sqlite3 as sql

   
 
try:
    with sql.connect("filmflix.db") as dbCon:
        dbCursor = dbCon.cursor()
except sql.OperationalError as e:
    print(f"connection failed: {e}")        