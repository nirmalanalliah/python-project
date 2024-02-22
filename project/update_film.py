from connect import *
 
def update_flims():
    try:
        
 
        flimID = int(input("Enter the FilmID to update a record: "))
        dbCursor.execute(f"SELECT * FROM tblfilms WHERE FilmID = {flimID}")
 
        #The fetchone fecthes a unique(one) record
        row = dbCursor.fetchone()
        #None is a single object to check if a value is present
        if row == None:
            print(f"No record with the FilmID {flimID} exists")
        else:
            fieldname = input("Enter the field (Title or YearReleased or Rating or Duration or Genre) ").title()
            fieldValue =input(f"Enter the value for {fieldname}: ")
           
            dbCursor.execute(f"UPDATE tblfilms SET {fieldname} = ? WHERE FilmID = ?",(fieldValue,flimID))
            dbCon.commit()
            print(f"{flimID} Updated")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")


if __name__ == "__main__":
    update_flims()
    

 