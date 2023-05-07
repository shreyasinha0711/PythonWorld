# Question:
# Armstrong Number ex: 153 : 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 1 + 125 + 27 = 153
# Find armstrong numbers between 200 to 400


for number in range(100, 400):
    # print(f"Number Checking {number}")
    duplicate_num = number
    armstrong_sum = 0
    rem = 0
    while duplicate_num > 0:
        rem = duplicate_num % 10
        armstrong_sum = armstrong_sum + rem * rem * rem
        duplicate_num = duplicate_num // 10
    if number == armstrong_sum:
        print(f"Armstong number is {number}")
