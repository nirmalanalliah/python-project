from connect import *

dbCursor.execute("""
CREATE TABLE "tblfilms" (
	"filmID"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"yearreleased"	INT,
    "rating" INT,
    "duration" INT,                        
	"genre"	TEXT,
	PRIMARY KEY("filmID" AUTOINCREMENT)
)""")
