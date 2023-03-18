import random

# random_integer = random.randint(1,10)

# print(random_integer)

# random_float = random.random()
# print(random_float)

# states_of_america = ["Delaware", "Oklahama", "Pennsylvania", "New Mexico"] 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
       _________)
        _________
       __________)
      (____)
---.__(___)
'''
print("Hello you are gonna play this game against the computer")

choice = input("What do you choose Rock, Paper or Scissor ?").lower()

if choice == "rock":
    print(rock)
    computer_choice = random.randint(0,2)
    if computer_choice == 0 :
        print(rock + "\n It's a draw try again!")
    elif computer_choice == 1 :
        print(paper + "\n You have lost")
    else:
        print(scissors + " \n Your Won!")
elif choice == "paper" :
    print(paper)
    computer_choice = random.randint(0,2)
    if computer_choice == 0 :
        print(rock + "\n You have Won!")
    elif computer_choice == 1 :
        print(paper + "\n  It's a draw try again!")
    else:
        print(scissors + "\n You have lost")
elif choice == "scissors":
     print(scissors)
     computer_choice = random.randint(0,2)
     if computer_choice == 0 :
        print(rock + "\n You have Lost!")
     elif computer_choice == 1 :
        print(paper + "\n You have Won!")
     else:
        print(scissors + "\n It's a draw try again!")


