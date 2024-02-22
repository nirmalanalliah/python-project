from connect import *
from read_film import *
 
def multiple_records():
        #create a list with the films to insert
        films = [insert into tblfilms(title, yearReleased, rating, duration, genre) 
                 values ('Golden Horizon', 2012, 4.5, '2 hours', 'western');
                 ('Lost in Translation', 2007, 3.3, '45 minutes', 'mystery');
                 ('Infinite Illusion', 2013, 2.6, '40 minutes', 'animation');
                 ('Dancing with Shadows', 2013, 3.9, '35 minutes', 'comedy');
                 ('Whimsical Wonderland', 2014, 4.7, '25 minutes', 'romance');
                 ('Dancing with Shadows', 2008, 4.5, '5 hours', 'adventure');
                 ('Infinite Illusion', 2015, 2.8, '30 minutes', 'mystery');
                 ('Lost in Translation', 2015, 3.2, '5 hours', 'documentary');
                 ('Serenade of Stars', 2019, 4.9, '25 minutes', 'adventure');
                 ('Whimsical Wonderland', 2020, 3.9, '2 hours', 'animation');
                 ('Serenade of Stars', 2013, 4.1, '5 hours', 'comedy');
                 ('Golden Horizon', 2011, 4.9, '25 minutes', 'drama');
                 ('Sapphire Symphony', 2017, 4.3, '30 minutes', 'western');
                 ('Violet Vortex', 2020, 4.7, '15 minutes', 'animation');
                 ('Enchanted Forest', 2012, 4.9, '20 minutes', 'adventure');
                
                ]
       
   
        # insert the records from the films list
        dbCursor.executemany("INSERT INTO tblfilms (Title,YearReleased,Rating,Duration,Genre) VALUES(?,?,?,?,?)", films)
        dbCon.commit()
        # now call the all_films function from the read_films file to display updated records
        all_films()
multiple_records()
 
     