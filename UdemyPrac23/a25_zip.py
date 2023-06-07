friends_list = ["Rolf", "ruth", "Jene", "charlie", "Jen"]
time_since_seen = [3, 7, 15, 11, 1]
long_timers = dict(zip(friends_list, time_since_seen))
print(long_timers)

long_timers = list(zip(friends_list, time_since_seen, [1, 2, 3, 4, 5]))
print(long_timers)
