# Anagram Program in Python

def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Strings are anagram")
    else:
        print("Not Anagram")


anagram("dog", "god")
