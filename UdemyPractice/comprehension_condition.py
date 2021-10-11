ages = [ 22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob","Rolf","Charlie", "michael"]

friend_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friend_lower.intersection(guests_lower))

present_friends = [
    name.title()
    for name in guests
    if name.lower() in friend_lower
]
print(present_friends)
