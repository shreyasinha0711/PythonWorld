lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        "name" : "Rolf",
        "number" : {13, 21, 2, 6}
    },
    {
        "name" : "Jose",
        "number" : {13, 21, 22, 8}

    }
]
name = players[0]["name"]
Player1_number = players[0]["number"]
Player1_lottery = lottery_numbers.intersection(Player1_number)
player1_lenth = len(Player1_lottery)
print(f"Player {name} got {player1_lenth} numbers right.")

name = players[1]["name"]
Player2_number = players[1]["number"]
Player2_lottery = lottery_numbers.intersection(Player2_number)
player2_lenth = len(Player2_lottery)
print(f"Player {name} got {player2_lenth} numbers right.")
"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
