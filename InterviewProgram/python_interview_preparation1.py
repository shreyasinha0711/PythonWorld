#add 2 tuples
t1 = ("A","B")
t2 = ("c", "d")
print("Adding the tuples: ", t1+t2)

#add 2 list
l1 = ["A", "B"]
l2 = ["C", "D"]
print(l1+l2) #['A', 'B', 'C', 'D']
l1.append(l2) 
print(l1) #['A', 'B', ['C', 'D']]
print(l2) #['C', 'D']

#get keys from dict
d1 = {"name": "Rold Smith", "age": 24}
for i in d1:
    print(i)

for i in d1.keys():
    print(i.title())
    print(i.capitalize())

#insert an element at given index in python
l = [10, 11, 1, 4]
l.insert(1, 5)
print(l)

#remove duplicates from list
rd = [ 10, 1, 1, 4, 3, 4, 5]
set_rd = set(rd)
print(set_rd)
rd_new = list(set_rd)
print(rd_new)


#list comprehension
ll = [ 10, 1, 1, 4, 3, 4, 5]
l2 = [n*2 for n in ll]
print("list comprehension")
print(l2)

l3 = [n*3 for n in ll if n % 2 == 0]
print("list comprehension with condition")
print(l3)

#dictionary like this -> d1={“k1″:10,”k2″:20,”k3”:30}, increment values of all the keys
d1 = {"k1":10, "k2":20, "k3":30, "k4":40, "k5":50}
for a in d1:
    d1[a] = d1[a]+1
print(d1)

#random number
import random

num = random.random()
print(num)
num2 = random.randint(1,15)
print(num2)

#byte convert
str = "shreya"
print(type(str))
bb = bytes(str, 'utf-8')
print(type(bb))

#object() function returns an empty object
x = object()


#docstring
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)


#decorators

#class in python
class Node(object):
    def __init__(self):
        self.x = 0
        self.y = 0

#init method in python
#__init__ is a method or constructor in Python.
# This method is automatically called to allocate memory when a new object/ instance of a class is created.
# All classes have the __init__ method.
#The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called.
class Employee:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = 2000

e1 = Employee("a",23, 20000)
print(e1.name, e1.age, e1.sal)

#lambda function
add = lambda x,y : x+y
print(add(2,3))

#randomize the item of a list
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

print("----------------------------------------------------")
#multi-level inheritance If class A inherits from B and C inherits from A it’s called multilevel inheritance.
class B(object):
    def __init__(self):
        self.b=0

class A(B):
    def __init__(self):
        self.a=0

class C(A):
    def __init__(self):
        self.c=0




