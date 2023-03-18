from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_cod,y_cod):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(7,1)
        self.goto(x=x_cod,y=y_cod)
        self.color("white")
        self.speed("fastest")

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(),self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(),self.new_y)
    



