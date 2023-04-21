friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print(friend_ages)

#order is mainted as of 3.7 but set don't have order

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)

#iteration over dict

#get keys
for name in friend_ages:
    print(name)

for ages in friend_ages.values():
    print(ages)

for name, ages in friend_ages.items():
    print(f"{name} is {ages} years old")



#dict comprehensions
print("-----DICT COMPREHENSIONS----")

friends = ["Rolf", "ruth", "Charlie", "Jen"]
time_since_seen = [3, 7, 14, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}
print(long_timers)


#zip function
print("-----ZIP FUNCTION----")
#combine list 
print(dict(zip(friends, time_since_seen)))
print(list(zip(friends, time_since_seen)))

print(list(zip(friends, time_since_seen, [1, 2, 3, 4, 5])))