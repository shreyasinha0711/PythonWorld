list_a = [1, 6, 7, 9]
list_b = [1,2,2,7,8,8,9]

set_a = set(list_a)
set_b = set(list_b)

if len(list_b) == len(set_b):
    print("True")
else:
    print("False")