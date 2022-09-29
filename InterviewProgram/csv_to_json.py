import json

dict_my = {}
list_my = []

with open("./files/my.csv", "r", encoding='utf-8-sig') as data:
    data_header = data.readline().rstrip('\n').split(',')
    print(data_header)
    for line in data:
        data_body = line.rstrip('\n').split(',')
        data_dict = dict(zip(data_header, data_body))
        list_my.append(data_dict)
    
    print(list_my)

out_file = open("./files/my_out.json", "w")
json.dump(list_my, out_file, indent= 4)


with open("./files/my.csv", "r", encoding='utf-8-sig') as data:
    first_line = data.readline().rstrip("\n").split(",")
    print(first_line)
    for line in data:
        data_line = line.rsplit('\n').split(',')
        print(data_line)