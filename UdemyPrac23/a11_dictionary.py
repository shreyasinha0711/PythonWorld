friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friends_ages["Rolf"])

friends_ages["Rolf"] = 26

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[0])
print(friends[0]["name"])




friends = [("Rolf", 24), ("Adam", 30)]
friends_ages = dict(friends)
print(friends_ages)