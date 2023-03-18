import turtle as t
import random

screen = t.Screen()
is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
turtle_set = ["tim","jack","may","lyn","zoe"]
color_set = ['green', "red","blue","orange","purple","yellow"]
y1 = -100
x = -150
set_chosen_color = []
all_turtle = []

for i in range(len(turtle_set)):
    y = turtle_set[i]
    y = t.Turtle()
    y.penup()
    y.shape("turtle")
    chosen_color = random.choice(color_set)
    
    for i in range(len(set_chosen_color)):
        if chosen_color  in set_chosen_color:
            chosen_color = random.choice(color_set)   
    set_chosen_color.append(chosen_color)  
    y.color(chosen_color)
    y.goto( y=y1, x=-230)
    y.pendown()
    y1 += 50   
    all_turtle.append(y) 
        
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won!")
            else:
                print("You have lost")
        rand_distance = random.randint(0,10)
        turtle.penup()
        turtle.forward(rand_distance)







screen.exitonclick()