print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"').lower()

if direction == "left":
    boat = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to sim across." ).lower()
    if boat == "wait":
        house = input("You arrive at th eisland unharmed. There is a house with 3 doors. One red, one yello one blue. Which colour do you chooose?").lower()
        if house == "blue":
            print("You enter a room of beasts. Game Over")
        elif house == "yellow":
            print("You enterd a room of Gold. You WIN")
        elif house == "red":
            print("You enterd a room of fire. You LOSE Game over")
    else:
        print("Game Over. you fell in a hole")
else:
    print("Game over")
