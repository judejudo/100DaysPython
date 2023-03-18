# def add(*args):
#     print(args)
#     sum = 0 
#     for n in args:
#         sum += n
#     return sum

# add(3,5,6,2)

# def calculate (n,**kwargs):
#     print(kwargs)
#     # this is a dictionary
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]


# calculate(add=3, multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")

print(my_car.model)