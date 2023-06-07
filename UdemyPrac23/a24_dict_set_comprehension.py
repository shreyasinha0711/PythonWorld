friends = ["Rolf", "ruth", "Jen", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# friends_lower = set([f.lower() for f in friends])
# guest_lower = set([g.lower() for g in guests])

friends_lower = {f.lower() for f in friends}
guest_lower = {g.lower() for g in guests}
present_friends = friends_lower.intersection(guest_lower)
present_friends = {n.title() for n in present_friends}

print(present_friends)


time_since_seen = [3, 7, 15, 11, 1]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)
