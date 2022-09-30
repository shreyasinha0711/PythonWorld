#check if all characters are alphanumeric
import re

str1 = "abcd123"
check1 = bool(re.match('[A-Za-z0-9]+$', str1))
print(check1)
str2 = "abcd123@@"
check2 = bool(re.match('[A-Za-z0-9]+$', str2))
print(check2)

#method 2
print("abcd123".isalnum())