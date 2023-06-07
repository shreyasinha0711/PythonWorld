age = 34
print(f"You are {age}")

name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)

name = "Bob"
greeting = f"How are you, {name}?"
print(greeting)


name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)


name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name="Jose")
print(jose_greeting)