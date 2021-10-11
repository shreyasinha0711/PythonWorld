def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!!")

greet()

car = {
    "make": "Ford",
    "model": "fiesta",
    "mileage": 23000,
    "fuel": 460
}

def cal_mpg():
    mpg = car["mileage"] / car["fuel"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")

cal_mpg()

def cal_mpg1(car_to_cal):
    mpg = car_to_cal["mileage"] / car_to_cal["fuel"]
    name = f"{car_to_cal['make']} {car_to_cal['model']}"
    print(f"{name} does {mpg} miles per gallon.")

cal_mpg1(
    {
        "make": "Ford",
        "model": "fiesta",
        "mileage": 23000,
        "fuel": 460
    }
)


car_all = [
    {"make": "Ford1", "model": "fiesta1", "mileage": 23000, "fuel": 460},
    {"make": "Ford2", "model": "fiesta2", "mileage": 23000, "fuel": 460},
    {"make": "Ford3", "model": "fiesta3", "mileage": 23000, "fuel": 460},
    {"make": "Ford4", "model": "fiesta4", "mileage": 23000, "fuel": 460}
]


def cal_mpgall(cars, intro):
    print(intro)
    mpg = cars["mileage"] / cars["fuel"]
    name = f"{cars['make']} {cars['model']}"
    print(f"{name} does {mpg} miles per gallon.")

for cars in car_all:
    cal_mpgall(cars, "new car!!")
