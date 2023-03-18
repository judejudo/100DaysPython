import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()