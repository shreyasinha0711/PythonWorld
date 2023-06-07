# age = int(input("Enter your age: "))
age = 25
result = age > 18 and age < 65
print(f"Result1 is {result}")

result = age < 18 and age < 65  # False and False
print(f"Result2 is {result}")

print(True and 18)

result = age > 18 or age < 65  # True and False
print(f"Result3 is {result}")

bool(0)  # False, zero
bool(13)  # True

bool("")  # False empty string
bool("Hello")  # True
bool([])  # False, empty list
bool([1, 3, 5])  # True


default_age = 30
age = 0

user_age = age or default_age
print(user_age)


default_greeting = "there"
name = input("Enter your name: ")

user_name = name or default_greeting
print(f"Hello, {user_name}")
