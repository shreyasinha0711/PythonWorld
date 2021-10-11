friends = ["Rolf", "John", "Anna"]

counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

for counter, friend in enumerate(friends, start=1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(list(zip([0, 1, 2], friends)))

print(dict(enumerate(friends)))
