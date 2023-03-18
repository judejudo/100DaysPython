# enemies = ("cow")
# def increase_enemies():
#     global enemies 
#     enemies = 2 
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# PI = 3.14159
# URL = "hrrps://ww.google.com"

# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
 
# a_function(10)
# print(a_variable)

# i = 50
# def foo():
#     i = 100
#     return i
 
# foo()
# print(i)

from art import logo_gues
import random 

print(logo_gues)

print("Welcome to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard: ")
guess = ""
def try_guess():
    global guess
    guess = int(input("Make a guess: "))
    return guess
random_number = random.randint(0,100)
number_of_attempts = 0
def attempts ():
    if mode == "easy":
        global number_of_attempts 
        number_of_attempts = 10
        return print(f"You have {number_of_attempts} attempts to guess the correct number.")
    elif mode  == "hard":
        
        number_of_attempts = 5
        return print(f"You have {number_of_attempts} attempts to guess the correct number.") 

def guessfun():
    global guess
    if guess > random_number:
        return print("Too high")
    elif guess < random_number:
        return print("Too low")
    elif guess == random_number:
        return print(f"You got it the answer is {random_number}"), exit()

trials = 0
attempts()
while trials < number_of_attempts:
    try_guess()
    guessfun()
    trials += 1
    if trials == number_of_attempts:
        print(f"You lose the correct number is {random_number}")
        





# print(logo_gues)
# def try_again():
#     play = input("Do you want to play again if yes 'y' if no 'n'")
#     if play == 'y':
#         play_again()
#     elif play == 'n':
#         return print("Thank you for playing the game see you next time!")
# def play_again():
#     print("Welcome to the Number guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     mode = input("Choose a difficulty. Type 'easy' or 'hard: ")
#     guess = ""
#     def try_guess():
#         global guess
#         guess = int(input("Make a guess: "))
#         return guess
#     random_number = random.randint(0,100)
#     number_of_attempts = 0
#     def attempts ():
#         if mode == "easy":
#             global number_of_attempts 
#             number_of_attempts = 10
#             return print(f"You have {number_of_attempts} attempts to guess the correct number.")
#         elif mode  == "hard":
#             number_of_attempts = 5
#             return print(f"You have {number_of_attempts} attempts to guess the correct number.") 

#     def guessfun():
#         global guess
#         if guess > random_number:
#             return print("Too high")
#         elif guess < random_number:
#             return print("Too low")
#         elif guess == random_number:
#             return print(f"You got it the answer is {random_number}"), try_again()

#     trials = 0
#     attempts()
#     while trials < number_of_attempts:
#         try_guess()
#         guessfun()
#         trials += 1
#         if trials == number_of_attempts:
#             print(f"You lose the correct number is {random_number}")
#             try_again()
            
            
# play_again()