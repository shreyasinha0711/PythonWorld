cars = ["ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("stopping....")
        break
    print(f"This car is {status}")

print("--------------------------------------------")
for status in cars:
    if status == "faulty":
        print("stopping....")
        continue
    print(f"This car is {status}")
    print("Shipping new car")
