import read_film,add_film, update_film, delete_film, search_film
 
def read_file(file_path): # file_path is a parameter/variable
    try:
         with open(file_path) as readfile:
             rf = readfile.read()
        #with open(file_path) as rf:
         #   rf.read()
             return rf
   
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
# Testing file path
print(read_file("project/menuOptions.txt"))      

def film_menu():
    option = 0 # initialise/assign the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"]
    # call the read_file function and assign to a variable(menu_choices)
    menu_choices = read_file("project/menuOptions.txt")
 
    # repeat the menu options until user select the to quit
    while option not in optionsList:
        print(menu_choices) # print the menu_choices variable because it is a function
        # re-assign the option variable a string value
        option = input("Enter an option from the menu choice above : ")
 
        # check if the input provided in options variable is not outside of 1,2,3,4,5,6
        if option not in optionsList:
            print(f"{option} is not a valid choice! ")
    return option

# testing
# print(film_menu())
# create and use a boolean flag Variable
mainProgram = True # toggle to False to exit out of the while loop
 
while mainProgram: # while True
     # call the songs_menu function and assign to a variable(main_menu)
    main_menu = film_menu()
 
    # use match case # same as swith in javascript
    match main_menu:
        case "1": # call the readsong file and the function display all songs
            read_film.all_films()
        case "2":
            add_film.insert_films()
        case "3":
            update_film.update_flims()
        case "4":
            delete_film.delete_films()
        case "5":
            search_film.search_films()
        case _:
            mainProgram = False # set mainProgram = False to exit the menu
input("Press enter to exit......")
 
 

 
