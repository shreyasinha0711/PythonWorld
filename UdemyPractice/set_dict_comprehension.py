friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friend_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

present_friends = friend_lower.intersection(guests_lower)
present_friends_title = {name.title() for name in present_friends}

print(friend_lower)
print(guests_lower)
print(present_friends)
print(present_friends_title)


friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)
