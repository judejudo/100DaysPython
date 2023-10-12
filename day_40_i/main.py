from sheety import Sheety

SHEETY_ENDPOINT="https://api.sheety.co/1fefdadf7650b71015a5c873b4339e02/copyOfFlightDeals1/users/"

print("Welcome to Angela's Flight Club. \n We find the best flight deals and email you.")
fname = input("What is your first name? ")
lname =  input("What is your last name? ")
email = input("What is your email address? ")
confirm_email = input("Please type your email again for confirmation. ")

id_count = 1

if email == confirm_email and fname != "" and lname != "":
  updated_data = {
       'user': {
         'firstName': fname,
         'lastName': lname,
          'email': email
          }
  }

  sheety = Sheety(SHEETY_ENDPOINT)
  print(sheety.update_data(data= updated_data))
