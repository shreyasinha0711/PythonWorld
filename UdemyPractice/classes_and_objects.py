a = True
b = False
c = True

if not a or b:
    print("a")
elif not a or not b and c:
    print("b")
elif not a or b or not b and a:
    print("c")
else:
    print("d")

print(not a or b)
print(not a or not b and c)
# not a = false or true and true

print(not a or b or not b and a)
# false or false or true and true
# false or true and true
# true and true



