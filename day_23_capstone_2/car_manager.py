from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_VALUE = range(-200,200)




class CarManager():
    def __init__(self) :
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            self.starting_pos = (280,random.choice(Y_VALUE))
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(self.starting_pos)
            self.all_cars.append(new_car)

            

    def move_left(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
