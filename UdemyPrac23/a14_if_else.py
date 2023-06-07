friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")
else:
    print("Hello, Stranger!!")
print("This runs anyway.")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]
user_name = input("enter the name: ")

if user_name in friends:
    print("Hello, Friend!!")
elif user_name in family:
    print("Hello, Family!!")
else:
    print("I don't know you")
