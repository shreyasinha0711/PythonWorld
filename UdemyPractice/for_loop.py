friends =["Rof", "Jen", "Anne"]

for friend in friends:
    print(friend)

elements = [0, 1, 2, 3, 4, 5, 6]
for index in elements:
    print("hello")

for i in range(2, 20, 2):
    print(i)

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Anne", "grade": 80},
    {"name": "Jen", "grade": 70},
    {"name": "An", "grade": 99},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has grade {grade}.")
