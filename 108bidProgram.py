from os import system, name
from art import logo_auction
def clear():
    if name == 'nt':
        _ = system('cls')



auctioner = {}
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        amount = int(bidding_record[bidder]) 
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print(bidding_record)
    
print(logo_auction)
print("Welcome to the secret auction program")
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    auctioner[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if answer == "no":
        bidding_finished = True
        find_highest_bidder(auctioner)
    elif answer == "yes":
        clear()
    


    