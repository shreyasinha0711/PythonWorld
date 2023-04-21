cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("stopping")
        break
    print(f"This car is {status}.")
    print(f"Shipping new car to customer.")


cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("Faulty on skipping")
        continue
    print(f"This car is {status}.")
    print(f"Shipping new car to customer.")

#without else

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
all_suc = True

for status in cars:
    if status == "faulty":
        print("Faulty on skipping")
        all_suc = False
        break
    print(f"This car is {status}.")
    print(f"Shipping new car to customer.")

if all_suc:
    print("All cars built succefully. No Faulty")

#with else

cars = ["ok", "ok", "ok", "ok", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Faulty on skipping")
        break
    print(f"This car is {status}.")
    print(f"Shipping new car to customer.")
else:
    print("All cars built succefully. No Faulty")