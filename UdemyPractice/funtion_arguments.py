cars = [
    {"make": "Ford1", "model": "fiesta1", "mileage": 23000, "fuel": 460},
    {"make": "Ford2", "model": "fiesta2", "mileage": 23000, "fuel": 460},
    {"make": "Ford3", "model": "fiesta3", "mileage": 23000, "fuel": 460},
    {"make": "Ford4", "model": "fiesta4", "mileage": 23000, "fuel": 460}
]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel"]
    return mpg

def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name

def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per gallon.")

for car in cars:
    print_car_info(car)


def divide(x,y):
    if y==0:
        return "divide by zero!!"
    else:
        return x / y

print(divide(10, 2))
print(divide(6, 0))
