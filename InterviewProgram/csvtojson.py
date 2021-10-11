import json
dict_a ={}
list_a = []
with open("./file/csv_data.txt", "r") as data:
    data_header = data.readline().rstrip('\n').split(',')
    print(data_header)
    for line in data:
        data_body = line.rstrip('\n').split(',')
        dict_b = dict(zip(data_header, data_body))
        list_a.append(dict_b)
    
    print(list_a)

out_file = open("./file/test2.json", "w")
json.dump(list_a, out_file, indent = 4)

