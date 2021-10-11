movie = {
    'name': 'The Matrix',
    'director': 'Watchowski'
}

class Movie:
    def __init__(self, movie_name, new_director):
        self.name = movie_name
        self.director = new_director

    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")

my_movie = Movie('The Matrix', 'Wachowski')
#print(my_movie.name)
#print(my_movie.director)

my_movie.print_info()
