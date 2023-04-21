def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet()


cars = [{
    "make": "Frod",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
},
{
    "make": "Frod1",
    "model": "Fiesta1",
    "mileage": 230001,
    "fuel_consumed": 4601
},
{
    "make": "Frod2",
    "model": "Fiesta2",
    "mileage": 230002,
    "fuel_consumed": 4602
}]


def calculate_mpg(car_to_cal):
    mpg = car_to_cal["mileage"]/car_to_cal["fuel_consumed"]
    return mpg
    

def car_name(car_to_cal):
    name = f"{car_to_cal['make']} {car_to_cal['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per gallon.")


for car in cars:
    print_car_info(car)


#other function
def divide(x, y):
    if y==0:
        return "You tried to divide by zero!"
    else:
        return x/y

print(divide(10,2))
print(divide(6,0))



#default paramter value
def add(x, y=3):
    total = x + y
    return total

print(add(5, 6))
print(add(5))

#named arguments
print(add(x=3))
#if first has name, then other must have name
print(add(x=5, y=2))
#first don't have then also fine, but once it start it should have for all subsequent parameters
print(add(5, y=12))

#print function

print(1, 2, 3, 4, 5, sep= ':')