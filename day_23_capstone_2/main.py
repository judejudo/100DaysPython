import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
turtle = Player()

screen.listen()
screen.onkey(key="w", fun=turtle.move_up)
turtle.move_up()

car = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_left()

    #Detect collision with car
    for vehicle  in car.all_cars:
        if vehicle.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect successful crossing
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car.level_up()
        scoreboard.increase_level()
    


    

screen.exitonclick()