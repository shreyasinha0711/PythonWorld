cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "focus", "mileage": 21000, "fuel_consumed": 490}
]


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def car_print(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per gallon.")


for car in cars:
    car_print(car)


def divide(x, y):
    if y==0:
        return "You try to divide by zero!!"
    else:
        return x / y


print(divide(4, 2))
print(divide(4, 0))
