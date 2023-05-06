num0 = 0
num1 = 1
num3 = 0

n = int(input("Enter the number of inputs for fibonacci series: "))


for num in range(n):
    if num == 0 or num == 1:
        print(num)
    else:
        num3 = num0 + num1
        print(num3)
        num0 = num1
        num1 = num3
