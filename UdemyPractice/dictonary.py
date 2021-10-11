friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25

print(friend_ages)

friends = (
    {"name": "Rold Smith", "age": 24},
    {"name": "Adam Wool", "age": 34},
    {"name": "Anne Pun", "age": 27},
)

print(friends[0])
print(friends[0]["name"])

friends = [("Rolf", 24),("Adam", 30),("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)

