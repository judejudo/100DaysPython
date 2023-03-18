from game_data import data
import random
from art import logo_higherlower,vs

print (logo_higherlower)
score = 0
game_should_continue = True
dataB = random.choice(data)

while game_should_continue:
    dataA = dataB
    dataB = random.choice(data)
    

    


    def data_choice(dic):
        return (f"{dic['name']}, {dic['description']}, {dic['country']}")
    def compare_followers(dic1,dic2,choice1):
        global score
        if dic1['follower_count'] > dic2['follower_count']:
            if choice1 == "a":
                score += 1
                return print(f"You're right! Current score: {score}.")
            else:
                global game_should_continue
                game_should_continue = False
                return print(f"Sorry, that's wrong. Final score:{score}.")
                
        elif dic2['follower_count'] > dic1['follower_count']:
            if choice1 == "b":
                score += 1
                return print(f"You're right! Current score: {score}.")
            else:
                game_should_continue = False
                return print(f"Sorry, that's wrong. Final score:{score}.")
                




    
    print(f"Compare A: {data_choice(dataA)}")
    print(vs)
    print(f"Against B: {data_choice(dataB)}")
    choice = input("Who has more followers? 'A' or 'B' :").lower()
    compare_followers (dataA,dataB,choice)



