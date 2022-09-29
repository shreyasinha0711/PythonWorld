with open("./files/my_out.json", "r") as f:
    count = 0
    data = f.read()
    for ch in data:
        if ch.isupper():
            count +=1

print(count)
    