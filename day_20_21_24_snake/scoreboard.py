from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier',20,'italic') 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("white")
        self.high_score = 0
        # with open("data.txt") as data:
        #     self.high_score = int(data.read())
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.style = ('Courier',20,'italic')
        self.write(f'Score: {self.point} High Score: {self.high_score}', align=ALIGNMENT,font=FONT )
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align=ALIGNMENT,font=FONT )

    def reset(self):
        if self.point > self.high_score:
            self.high_score = self.point
            # with open("data.txt", mode="w") as data:
            #     data.write(f"{self.high_score}")
        self.point = 0
        self.update_scoreboard()

        

    def update_score(self):
        self.point += 1
        self.update_scoreboard()
        



        
        
        
        


