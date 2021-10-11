cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print(".......Stop production.........")
        break
    print(f"Car status: {status}")
    print("Shipping!!")
else:
    print("All car build sucessfully. No Faulty cars!!")
