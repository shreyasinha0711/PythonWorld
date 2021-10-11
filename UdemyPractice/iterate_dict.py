friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

for name in friend_ages:
    print(name)

for age in friend_ages.values():
    print(age)

for name,age in friend_ages.items():
    print(f"{name} : {age}")
