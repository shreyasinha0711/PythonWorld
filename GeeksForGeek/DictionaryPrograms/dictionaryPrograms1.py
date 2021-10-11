keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict_a = dict(zip(keys, values))
print(dict_a)

#Delete set of keys from a dictionary
sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
keysToRemove = ["name", "salary"]

for keys in keysToRemove:
    sampleDict.pop(keys)

print(sampleDict)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#Expected output:

#['My', 'name', 'is', 'Kelly']
list3 =[]
for i in range(0,4):
    var = list1[i]+list2[i]
    list3.append(var)
print(list3)
    
