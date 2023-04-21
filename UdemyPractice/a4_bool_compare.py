truthy = True
falsy = False
age = 20
is_over_age = age >= 18
print(is_over_age)
is_under_age = age < 18
print(is_under_age)
is_twenty = age == 20
print(is_twenty)

my_num = 5
user_num = int(input("Enter a number: "))
print(my_num == user_num)

matches = my_num == user_num
print(f"You got it right: {matches}")


# and or 

age = int(input("Enter your age : "))
can_learn_programming = age > 0 and age < 150
print(f"You can learn program: {can_learn_programming}")

usually_working = age > 18 or age < 65
print(f"At {age}, you working {usually_working}")

print(bool(35))
print(bool(0)) #false
print(bool("")) #false

#and gives you 2nd value if it is true 1st else second value
x = 35 and 0
print(x)  #gives 2nd vale value

x = 0 and 35
print(x)  #gives 1st vale value as false

 # or gives you first value if it is true else second value

x = 0 or 35
print(x)  #gives 2nd vale value

x = 35 or 0
print(x)  #gives 1st vale value

name = input("Enter name: ")
surname = input("Enter your surname: ")

greet = name or f"Mr. {surname}"
print(greet)


