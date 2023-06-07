cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
all_successful = True

for status in cars:
    if status == "faulty":
        print("stopping....")
        all_successful = False
        break
    print(f"This car is {status}")
    print("Shipping...")

if all_successful:
    print("All cars are sucessful.")


print("------------------------------------------")

for status in cars:
    if status == "faulty":
        print("stopping....")
        break
    print(f"This car is {status}")
    print("Shipping...")

else:
    print("All cars are successful.")