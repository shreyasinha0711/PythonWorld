"""
Write a program to find the prime numbers between 100 to 200
"""

for num in range(100, 200):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

