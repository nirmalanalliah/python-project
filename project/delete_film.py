from connect import *
 
def delete_films():
    try:
        #check if the film id exists
        filmID  = int(input("Enter the FilmID to delete a record : "))
        dbCursor.execute(f"SELECT * FROM tblfilms WHERE FilmID = {filmID}")
 
        row = dbCursor.fetchone()
 
        if row == None:
            print(f"FilmID {filmID} does not exits")
        else:
            dbCursor.execute("DELETE FROM tblfilms WHERE FilmID = ?", (filmID,))
            dbCon.commit()
            print(f"The record {filmID} deleted from the tblfilms table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")
   

if __name__ == "__main__":
    delete_films()
   