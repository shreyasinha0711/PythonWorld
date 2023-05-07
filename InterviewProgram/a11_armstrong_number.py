# Question:
# Armstrong Number ex: 153 : 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 1 + 125 + 27 = 153


num = 153
num1 = num
sum = 0
while num1 > 0:
    rem = num1 % 10
    sum = sum + rem * rem * rem
    num1 = num1 // 10

if sum == num:
    print("!! Armstrong Number !!")
else:
    print("!! Not Armstrong Number !!")
