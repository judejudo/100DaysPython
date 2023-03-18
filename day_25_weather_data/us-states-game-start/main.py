import turtle
import pandas

ALIGNMENT = "center"
FONT = ('Courier',10,'italic') 


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day_25_weather_data/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("day_25_weather_data/us-states-game-start/50_states.csv") 

state = data["state"].to_list()

guessed_states =  []
city_not_named = []



while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)/50}Guess the state's name?", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        city_not_named = [n for n in guessed_states if n not in state] 
        # for item in guessed_states:
        #     for city in state:
        #         if item != city:
        #             city_not_named.append(city)
        
   
        data_dict = {
            "city":city_not_named
        }
        data1 = pandas.DataFrame(data_dict)
        data1.to_csv("cities_not_name.csv")

        
        break
    

    if answer_state in state:
        guessed_states.append(answer_state)
        if answer_state == answer_state:
            state_name = turtle.Turtle()
            state_name.penup()
            state_data = data[data.state == answer_state]
            state_name.goto(int(state_data.x), int(state_data.y))
            state_name.pendown()
            state_name.write(answer_state, align=ALIGNMENT,font=FONT)
            state_name.hideturtle()

        

turtle.mainloop()

