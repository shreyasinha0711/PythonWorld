num = 6
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")


#find all perfect number in betwwen 1 to 100

for num in range(1, 1001):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    
    if sum == num:
        print(f"{num} is perfect")
    
