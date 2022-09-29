#Reverse the statement

statement_input = input("Enter the Statement: ")
statement_reverse = ""
words = statement_input.split()

for word in words:
    statement_reverse = word + " " + statement_reverse

print(f"The reversed Statement: {statement_reverse}")

#Reverse the statement using reversed and join
statement_reverse_reversed = " ".join(reversed(words))
print(f"The reversed Statement using reversed: {statement_reverse_reversed}")



#remove space from the statement
statement = " This has     a     loads      of spaces      "
print(' '.join(statement.split()))