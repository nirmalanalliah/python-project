from connect import *
 
def all_films():
    try:
        # try to execute the sql statement below
        # dbCursor.execute("SELECT * FROM films")
 
        all_flims = dbCursor.execute("SELECT * FROM tblfilms").fetchall()
 
        # fetch all selected data(rows)
        # all_films = dbCursor.fetchall() # Fetchall fetches all the rows from the table
        all_flims = dbCursor.execute("SELECT * FROM tblfilms").fetchall()
        if all_flims:
            # format output
            print("FilmID | Title | YearReleased | Rating | Duration | Genre")
            print("*" * 50)
 
            for films in all_flims:
                print(f"{films[0]:<7} | {films[1]:<10} | {films[2]:<7} | {films[3]:<5}")
        else:
            print("No films found in the tblfilms table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
    finally:
        print("DB operation performed")


if __name__ == "__main__":
    all_films()
    