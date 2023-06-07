def greet():
    print("Hello")


hello = greet
hello()

average = lambda sequence: sum(sequence) / len(sequence)
total = lambda sequence: sum(sequence)
top = lambda sequence: max(sequence)

operations = {
    "avg": average,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (76, 80, 91, 60)},
    {"name": "Jen", "grades": (98, 68, 97, 80)},
    {"name": "Anne", "grades": (56, 91, 90, 90)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter avg, total or top: ")
    operation_function = operations[operation]
    print(operation_function(grades))
