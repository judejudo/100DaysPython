# print("Hello"[0])

# num_char = len(input("What is your name?"))

# new_str = str(num_char)

# print("Your name contain " + new_str + " characters")  

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = (percentage/100)*bill
new_bill = tip + bill
split=int(input("How many people to split the bill? "))

bill_each_person = round(new_bill/split, 2)

print(f"Each person should pay: ${bill_each_person}")




