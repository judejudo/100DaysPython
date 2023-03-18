from turtle import Turtle
X_AXIS = [20,40,60]
MOVE_DISTANCE = 20
UP =  90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self) :   
        self.snake = ['sq1','sq2','sq3'] 
        
        self.i=0
        for turtle in self.snake:
            turtle = Turtle()
            turtle.color("white")
            turtle.penup()
            turtle.shape("square")
            turtle.goto(y=20, x=X_AXIS[self.i])
            self.segment.append(turtle)
            self.i += 1

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)


    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading()!= RIGHT:
         self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)
      
    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)


    # def add_segment(self,position):
    
    # def extend(self)






