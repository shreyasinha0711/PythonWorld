friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

#dict([("Rolf", 3),("Bob", 7), ("Jen", 15), ("Anne", 11)])
#use zip to convert friends and time_since_seen to above one format

#get something like this ('Rolf', 3)
long_timers = dict(zip(friends,time_since_seen))
print(long_timers)

#get something like this ('Rolf', 3, 1)
long_timers = list(zip(friends,time_since_seen, [1, 3, 5, 7, 9]))
print(long_timers)
