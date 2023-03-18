from unittest import result
from art import logo_blackjack
import random
answer = input("Do you want to play a game of Blackjack? 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer = []
player = []

random_number = random.choice(cards)
computer.append(random_number)

def computercard():
    random_number = random.choice(cards)
    computer.append(random_number)


count_is_2 = False
while not count_is_2 :
    random_number = random.choice(cards)
    player.append(random_number)
    if len(player) == 2:
        count_is_2 = True
def playercard():
    """return score"""
    # result =0
    result = sum(player)
    
    print(f"Your cards:{player},current score:{result}")
    print(f"Computer's first card: {computer[0]}")
    random_number = random.choice(cards)
    player.append(random_number)
    if result > 21:
        print(f"Your have lost the computer wins") 
        exit()
    answer2 = input("Type 'y' to get another card, type 'n' to pass: ")
    if answer2 == 'y':
            playercard()
    elif answer2 == 'n':
        print(f"Your final score is {result}")
        result2 = 0
        while result2 < result:
            computercard()
            result2 = sum(computer)
        print(computer)
        print(f"Computer's  final score is {result2}")
        print("The computer wins ")
        if result2  > 21:
            print("You have won")

        
        
        
print(logo_blackjack)      
playercard()


