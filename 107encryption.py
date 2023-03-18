# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with(location="Jude", name="Nairobi")

from operator import index
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(word, jump, choice):
    
    if choice == "encode":
        encrypted_text1 = ""
        for i in word:
            if i in alphabet:
                index = alphabet.index(i)
                position = index + jump
                encrypted_text1 += alphabet[position] 
            else:
                encrypted_text1 += i 
        remainder =  (len(alphabet))%jump
        jump += remainder
        
        print(f"The encoded text is {encrypted_text1}")
    elif choice == "decode":
        decrypt_text1 = ""
        for i in word:
            index = alphabet.index(i)
            position = index - jump
            decrypt_text1 += alphabet[position]
        remainder =  (len(alphabet))%jump
        jump += remainder
        
        print(f"The decoded text is {decrypt_text1}")


      
end_of_game = False
while end_of_game == False: 


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    
    result = input("Do you want to continue? 'YES' or 'NO'.").lower()
    if result == 'yes':
        end_of_game == True
    elif result == 'no':
        end_of_game == False
        print("Goodbye")


