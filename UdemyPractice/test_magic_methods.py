# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, i):
        return self.players[i]

    def __str__(self):
        return f"Club {self.name} with {len(self)} players"


some_club = Club('Arsenal')
some_club.players.append('Rolf')
some_club.players.append('Anne')

