friend = "Rolf"
user_name = input("Enter your name: ")
if user_name == friend:
    print("Hello, friend!")
    print("this also runs")
else:
    print("Hello, Stranger!!")
print("This always runs.")


friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, Friend!!")
elif user_name in family:
    print("Hello, Family!!")
else:
    print("Hello, Stranger!!")