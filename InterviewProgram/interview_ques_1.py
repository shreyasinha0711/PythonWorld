import random

print(random.random())
print(random.randrange(1, 10, 2))


st = "Hi, m joy not joy but joy"
print(st.replace("joy","Joy"))

#convert a list into a string
weekdays = ['sun', 'mon', 'tues', 'thru', 'fri', 'sat']
listasString = ''.join(weekdays)
print(listasString)

#convert a list into a tuples
weekdays = ['sun', 'mon', 'tues', 'thru', 'fri', 'sat']
listasTuples = tuple(weekdays)
print(listasTuples)

#to count the occurrences of a particular element in the list
weekday = ['sun', 'sun', 'mon', 'tues', 'thru', 'fri', 'sat']

print(weekday.count("sun"))
#2
print([[x, weekday.count(x)] for x in weekday])
#[['sun', 2], ['sun', 2], ['mon', 1], ['tues', 1], ['thru', 1], ['fri', 1], ['sat', 1]]

#find the output
names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])
#n

#enumerate funtion
subjects = ('Python', 'Interview', 'Questions')
for i, sub in enumerate(subjects):
    print(i,sub)

#0 Python
#1 Interview
#2 Questions

list1 = [1,2,3]
print(list1 * 2)    
#[1, 2, 3, 1, 2, 3]



#function to take no of arguments
def func_arguments(*args):
    for i in args:
        print(i, end = " ")
    print()


func_arguments(1)
func_arguments(1,2,3,4)


import re
str1 = "abbbc"
check_1 = bool(re.match('ab{4,8}', str1))
print(check_1)



