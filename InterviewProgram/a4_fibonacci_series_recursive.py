num1 = 0
num2 = 1
range_input = int(input("Enter the range for fibonacci series: "))

def fibonacci(number):
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number -2)


for i in range(range_input):
    print(fibonacci(i))
