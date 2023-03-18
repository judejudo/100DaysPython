import turtle as t

tim = t.Turtle()
screen = t.Screen()



def move_forwards():
    return tim.forward(10)

def move_backward():
    return tim.backward(10)

def turn_left():
    return tim.left(90)

def turn_right():
    return tim.right(90)

def clear_screen():
    tim.penup()
    tim.goto(0,0)
    return tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.listen()
screen.exitonclick()