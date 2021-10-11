#first class function are those which can be assigned to a variables and used.

def greet():
    print("Hello")

hello = greet
hello()

#example 2
avg = lambda seq : sum(seq) / len(seq)
total = lambda seq : sum(seq)
top = lambda  seq : max(seq)

operations = {
    "avg" : avg,
    "total" : total,
    "top": top
}
#combine above 2
operations = {
    "avg" : lambda seq : sum(seq) / len(seq),
    "total" : sum,
    "top": max
}
students = [
    {"name": "Rolf", "grades": (67,90,95)},
    {"name": "Rolf", "grades": (68,60,75)},
    {"name": "Rolf", "grades": (69,70,85)},
    {"name": "Rolf", "grades": (65,80,65)}
]

for student in students:
    name = student["name"]
    grades = student ["grades"]
    print(f"Student: {name}")
    operation = input("Enter avg, total, top: ")
    operation_fun = operations[operation]
    print(operation_fun(grades))
