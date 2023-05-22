# Python program to remove character from string
# Input String: Quescol
# Input Character : e
# Output: Quscol (After removing ‘e’)


str1 = "Quescol"
print(str1)
ch = 'e'
print(str1.replace(ch, ""))


# using list method
str2 = "Quescole"
liststr = []
for c in str2:
    liststr.append(c)

print(liststr)

for c in liststr:
    if c == 'e':
        liststr.remove(c)

print(liststr)

print("".join(liststr))
