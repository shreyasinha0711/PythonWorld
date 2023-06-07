ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = ["Rolf", "ruth", "Jen", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]
guest_lower = [g.lower() for g in guests]

present_friends = [
     name.title() for name in guest_lower if name in friends_lower
]

present_friends = [
    name.title()
    for name in guest_lower
    if name in friends_lower
]
print(present_friends)
