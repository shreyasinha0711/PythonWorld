#Reverse the string

string_input = input("Enter the String: ")
string_reverse = ""

for c in string_input:
    string_reverse = c + string_reverse

print(f"The reversed String: {string_reverse}")

#palindrome

if string_input == string_reverse:
    print("Palindrome!!")
else:
    print("Not Palindrome!!")

#reverse string using inbuild properties -- slice
string_reverse_slice = string_input[::-1]
print(f"The reversed String using slicing: {string_reverse_slice}")


#reverse string using inbuild properties -- join and reversed function

string_reverse_reversed = "".join(reversed(string_input))
print(f"The reversed String using reversed function: {string_reverse_reversed}")


#reverse string using recursion

def reverse_string_rec(string_input):
    if len(string_input) == 0:
        return string_input
    else:
        return reverse_string_rec(string_input[1:]) + string_input[0]


print(f"The reversed string using recursion function: {reverse_string_rec(string_input)}")
