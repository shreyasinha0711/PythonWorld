# Python program to remove vowels from string
# Input String: Quescol
# Output: Qscl (After removing ‘e’)

str1 = "Quescol"
vowel = ('a', 'e', 'i', 'o', 'u')
result = ''


for ch in str1:
    if ch.lower() in vowel:
        ch = ''
    result = result + ch

print(result)

