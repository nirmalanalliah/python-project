from connect import *
 
def insert_films():
    try:
 
       
        title = input("Enter film Title: ")
        yearReleased = input("Enter film yearReleased: ")
        rating = input("Enter film rating: ")
        duration=input("Enter film Duration:")
        genre=input("Enter film Genre:")

        dbCursor.execute("INSERT INTO tblfilms VALUES(NULL,?,?,?,?,?)", (title,yearReleased,rating,duration,genre))
        dbCon.commit()
        print(f"{title} inserted in the tblfilms table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    except sql.Error as er:
        print(f"This error occurs: {er}")    


if __name__ == "__main__":
    insert_films()