friends = ["Rolf", "John", "Anna"]

index = 0

for friend in friends:
    print(index)
    print(friend)
    index = index + 1

counter = 0

for counter, friend in enumerate(friends, start=1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))
