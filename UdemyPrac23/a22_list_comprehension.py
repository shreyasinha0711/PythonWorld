numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append((number * 2))

print(doubled_numbers)


doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

doubled_numbers = [n * 2 for n in range(5)]
print(doubled_numbers)

friend_age = [22, 32, 35, 37]
age_string = [f"My friend is {age} old." for age in friend_age]
print(age_string)


names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)


friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends.")
