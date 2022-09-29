num = 153
num1 = num
sum = 0
while num1 > 0:
    rem = num1 % 10
    sum = sum + rem * rem * rem
    num1 = num1 // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")