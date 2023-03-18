import random
import hangman_words
from hangman_art import stages, logo

print(logo)

picked_word = ""

choice_word = random.choice(hangman_words.word_list)
picked_word += choice_word
display = []
life = 6


end_of_game = False
for n in picked_word:
     display.append("_")
while end_of_game == False :
    guess = input("Geuss a letter ").lower()
    if guess in display:
      print(f"The letter is alread guessed{guess}")
    picked_word_length = len(picked_word)
    for n in range(picked_word_length):
        letter = picked_word[n]
        if letter == guess:
            display[n] = letter
    if guess not in picked_word:
        print("You picked a wrong letter hence you loze one life")
        life -= 1
        for art in range(len(stages)):
            if art == life:
                print(stages[art])

    print(display)
    print(life)
    if life == 0:
        print("You lose")
    
    if ("_" not in display) :
        end_of_game = True
print("You won!")
print(f"{''.join(display)}")

