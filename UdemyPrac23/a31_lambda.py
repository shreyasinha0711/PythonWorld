divide = lambda x, y: x / y
print(divide(4, 2))


average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (76, 80, 91, 60)},
    {"name": "Jen", "grades": (98, 68, 97, 80)},
    {"name": "Anne", "grades": (56, 91, 90, 90)}
]

for student in students:
    print(average(student["grades"]))
