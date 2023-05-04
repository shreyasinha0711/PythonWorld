# Take the input from user
# Reverse the digit and check if palindrome number


num_input = int(input("Enter the number: "))

num_cp = num_input
num_reverse = 0

while num_cp != 0:
    rem = num_cp % 10
    num_reverse = num_reverse * 10 + rem
    num_cp = num_cp // 10


print(f"The reversed Number: {num_reverse}")

#palindrome
if num_input == num_reverse:
    print("Palindrome!!")
else:
    print("Not Palindrome!!")
