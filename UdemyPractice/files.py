my_file = open('file/data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name:')
#w :deletes the content previously present
my_file_writing = open('file/data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()

