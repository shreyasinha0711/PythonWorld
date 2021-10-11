#aa = input("Enter 2 binary")

aa ="110011,1010"
line = aa.rstrip("\n").split(',')
print(line)
a = line[0]
b = line [1]
print(type(a))
a = "110011"
b = "1010"
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)
  
# Initialize the result
result = ''
  
# Initialize the carry
carry = 0
  
# Traverse the string
for i in range(max_len - 1, -1, -1):
    r = carry
    r += 1 if a[i] == '1' else 0
    r += 1 if b[i] == '1' else 0
    result = ('1' if r % 2 == 1 else '0') + result
  
    # Compute the carry.
    carry = 0 if r < 2 else 1
  
if carry != 0:
    result = '1' + result
  
print(result.zfill(max_len))