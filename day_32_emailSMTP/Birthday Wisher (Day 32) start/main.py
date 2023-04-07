# import smtplib

# my_email = "angedujude@gmail.com"
# password = "hzwbkthloouxdclm"

# with smtplib.SMTP("smtp.gmail.com") as  connection: #email server
#     connection.starttls()#encrypting out mail
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ocomilj@gmail.com",
#         msg="Subject:Greetings\n\n Hello Jude")

import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:

    with open ("day_32_emailSMTP\Birthday Wisher (Day 32) start\quotes.txt", mode = "r") as data:
        data_list = data.readlines()
        random_quote = random.choice(data_list)

    my_email = "angedujude@gmail.com"
    password = "hzwbkthloouxdclm"
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr = my_email,
                        to_addrs ="newtonbryan12428@gmail.com",
                        msg = f"Subject:Wensday Motivation\n\nGood morning Newton Brian,\n{random_quote}.\nKeep striving for the best only,\nKind regards,\nJude Ang'edu" )

        