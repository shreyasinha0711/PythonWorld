is_learning = True

while is_learning:
    print("You're learning!!")
    user_input = input("Are you still learning?")
    is_learning = user_input == "yes"


user_input = input("Run pg(yes/no): ")
while user_input == "yes":
    print("We are running")
    user_input = input("Run pg(yes/no): ")

print("Stopped")