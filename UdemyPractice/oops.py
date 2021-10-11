my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88 ,90 ,99],
    'average': None
}

def avg(student):
    return sum(student['grades']) / len(student['grades'])

#print(avg(my_student))
#oops
#double underscore function are dunder function
#self is empty blank object that is created before the init funtion

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88 ,90 ,99])
student_two = Student('Rolf Smith 2', [70, 88 ,90 ,99])

print(student_one.name)
print(student_two.name)

print(student_one.average())
print(student_two.average())

#print(Student.average()) #error, agr missing
print(Student.average(student_one))


#paramter naming in python for oops
#self.name name is new property created inside self
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
matrix = Movie('The Matrix', 1994)
print(matrix.name)

