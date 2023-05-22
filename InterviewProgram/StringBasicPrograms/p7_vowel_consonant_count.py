# Python program to find count of vowels  and consonants from string
# Input String: Quescol
# Output: Vowels:3 Consonant: 4

str1 = "Quescol".lower()
vowels = ('a', 'e', 'i', 'o', 'u')

vowel_count = 0
consonant_count = 0

for ch in str1:
    if ch in vowels:
        vowel_count += 1
    else:
        consonant_count += 1


print(vowel_count, consonant_count)
