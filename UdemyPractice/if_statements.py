friend = "Rolf"
user_name = input("Enter the name: ")

if user_name == friend:
    print("Hello, Friend!!")
    print("This run too!!")
else:
    print("Hello, Stranger!!")
print("This runs anyway.")

print(bool(5))


friends = ["Rolf", "Bob", "Anne"]
family = ["Rol", "Bo", "Ann"]
user_name = input("Enter the name: ")

if user_name in friend:
    print("Hello, Friend!!")
elif user_name in family:
    print("Hello, Family!!")
else:
    print("Hello, Stranger!!")
