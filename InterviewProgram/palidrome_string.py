str1 = 'madam'
str2 = ''
str2 = ''.join(reversed(str1))

if(str1 == str2):
    print("Palin")
else:
    print("Non Palin")

test_str = "GeeksforGeeks"
all_freq = {} #dict
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print(all_freq)

for c in all_freq:
    if all_freq[c] > 1:
        print(c, end=" ")

























