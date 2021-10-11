import json

file = open('file/friends_json.txt', 'r')
file_contents = json.load(file)

print(file_contents)

file.close()
print('\n')
print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

#Go and insvestigate how to use json.dump

file = open('file/cars_json.txt', 'w')
json.dump(cars, file)
file.close()


my_json_string = '[{"name": "Alfa", "released": 1950}]'


incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
