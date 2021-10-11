numbers = [0, 1, 2, 3, 4]
doubled_nums = []

for number in numbers:
    doubled_nums.append(number * 2)

print(doubled_nums)

doubled_nums = [number * 2 for number in numbers]
print(doubled_nums)

doubled_nums = [2 for number in range(5)]
print(doubled_nums)

doubled_nums = [2 for _ in range(5)]
print(doubled_nums)

friend_ages = [22, 33, 45, 54]
age_strings = [f"My friend is {age} years old." for age in friend_ages]
print(age_strings)

names = ["Rolf", "Jane", "Bob"]
lower = [name.lower() for name in names]
print(lower)

friend = input("Enter the user name: ")
friends = ["Rolf", "Jane", "Bob"]
friend_lower = [name.lower() for name in friends]

if friend.lower() in friend_lower:
    print(f"{friend.title()} is one of your friends.")
