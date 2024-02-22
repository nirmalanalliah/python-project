from connect import *
def search_films():
        try:
                #ask for the field to search by
            field = input("Search by YearReleased,Rating,Genre : ")
 
            if field == "filmID":
                # search by FilmID
                idInput = int(input("Enter FilmID: "))
                dbCursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (idInput,))
                row = dbCursor.fetchone()
 
                if row is None:
                    # if the FilmID entered is not in the table
                    print(f"No record with FilmID {idInput} exists")
                else:
                    # if the FilmID entered is exiata in the table
                    for film in row:
                        print(film)
 
            elif field in ["yearReleased","rating","genre"]:
                # search by Title,YearReleased,Rating,Duration,Genre
                strInput= input(f"Enter the value for the field {field}: ")
                #SELECT * FROM tblfilms WHERE  "yearReleased", "rating" ,"genre" LIKE "comedy" or "Action" or "Fantasy"  ?
 
                dbCursor.execute(f"SELECT * FROM tblfilms WHERE {field} LIKE '%{strInput}%'")
                # dbCursor.execute(f"SELECT * FROM tblfilms WHERE {field} LIKE '", (f"'%{strInput}%"))
                rows = dbCursor.fetchall()
                if not rows:
                    print(f"No record with field {field} matching {strInput} ")
 
                                    # display all matched records for the search field
                elif field == "rating" or field == "yearReleased":
                    for records in rows:
                        print(records)

                
                else:
               
                    if field == "genre":
                        gInput1 = input("Enter the first Genre:")
                        gInput2 = input("Enter the Second Genre:")
                        dbCursor.execute(f"SELECT * FROM tblfilms WHERE Genre = '{gInput1}' OR Genre = '{gInput2}' ")
 
                        genreTypes = dbCursor.fetchall()
                        for gType in genreTypes:
                            print(gType)
                    else:
                        print(f" No match found for {gInput1} or {gInput2} ")
 
 
 
            else: # where the search input is not YearReleased,Rating,Genre
                print(f"Search field {field} invalid !")
        except sql.OperationalError as e:
            print(f"Failed because: {e}")
        except sql.ProgrammingError as pe:
            print(f"Not working because: {pe}")
        finally:
            print("DB operation performed")
search_films()            



