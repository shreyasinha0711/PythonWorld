cars = [{
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
},
{
    "make": "Ford",
    "model": "focus",
    "mileage": 21000,
    "fuel_consumed": 490
}]


def calculate_mpg(car, intro):
    print(intro)
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} iles per gallon.")

for car in cars:
    calculate_mpg(car, "New Car")

