file = open('file/csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].upper()
    print(f'{name} is {age} old, studying {degree} at {university}.')

sample_csv_Value = ','.join(['Rolf','25','MIT','CS'])
print(sample_csv_Value)
