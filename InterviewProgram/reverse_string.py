str1 = 'shreyareverse'
#method1
rev1 = ''
for i in str1:
    rev1 = i + rev1
print("Reverse method 1 : "+ rev1)

#method2 -- recursive
def rev2(str1):
    if len(str1) == 0:
        return str1
    else:
        return rev2(str1[1:]) + str1[0]

print("Reverse method 2 : " + rev2(str1))


#method3 --join
rev3 = ''.join(reversed(str1))
print("Reverse method 3 : " + rev3)
