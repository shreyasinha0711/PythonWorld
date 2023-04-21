
"""Helo, world

My name is Shreya. leaving a multiline comment
"""
my_String = "Hello, world!"
my_String = 'Hello, world!'
print(my_String)
print("Hello's, wolrd")
another_with_quotes ='He said "you are amazing!!" yesterday.'
print(another_with_quotes)
another_with_quotes ="He said \"you are amazing!!\" yesterday."
print(another_with_quotes)

multiline = """Helo, world

My name is Shreya.
"""

print(multiline)

name = "jose"
greeting = "hello, " + name
print(greeting)

#string formatting
age = 34
agr_str = str(age)
print("you are " + agr_str)
print(f"you are {age}")  #no required to conver to str

greeting = f"How are you, {name} ?"
print(greeting)

name = "jose"
print(greeting)

final_greeting = "How are you, {} ?"
jose_greet = final_greeting.format(name)
print(jose_greet)
print(final_greeting.format(name))
name = "bob"
jose_greet = final_greeting.format(name)
print(jose_greet)

final_greeting = "How are you, {name} ?"
jose_greet = final_greeting.format(name="jose")
print(jose_greet)