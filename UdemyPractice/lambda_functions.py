#lambad functions are used to take input and return output.
"""
def divide(x, y):
   return x / y
"""

# lambda x, y --> are input and after : is retun
divide = lambda x, y: x / y
print(divide(15, 3))

print((lambda x, y: x / y)(15, 3))

#example 2

def average(sequence):
    return sum(sequence) / len(sequence)

#convert to lambda function
average = lambda sequence : sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67,90,95)},
    {"name": "Rolf", "grades": (68,60,75)},
    {"name": "Rolf", "grades": (69,70,85)},
    {"name": "Rolf", "grades": (65,80,65)}
]

for student in students:
    print(average(student["grades"]))

