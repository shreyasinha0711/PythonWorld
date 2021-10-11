#menu prompt for user
MENU_PROMPT = "\nEnter 'a' To Add Movie, 'l' To List Movie, 'f' To Find Movie By Title, 'q' To Quit\n"
movies = []

#take inputs from user
def add_movie():
    title = input("Enter Movie Title: ")
    director = input("Enter Movie Director Name: ")
    year = input("Enter Movie Year: ")

#add the movie inputs to the dictonary list
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

#list and show Movie function
def show_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

#find Movie function
def find_movie():
    search_title = input("Enter the Movie Title Name to find: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)

#user option mapping
user_options = {
    "a": add_movie,
    "l": show_movie,
    "f": find_movie
}

def menu():
    selection = input(MENU_PROMPT)
    while selection!= "q":
        if selection in user_options:
            selection_function = user_options[selection]
            selection_function()
        else:
            print("Unknown command. Please Try Again")
        selection = input(MENU_PROMPT)

menu()
