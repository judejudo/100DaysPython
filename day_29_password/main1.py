from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pas():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters)for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = " ".join(password_list)

    password_entry.insert(0, password)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.askokcancel(title=website, message=f"Email:{email} \nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
   
            #                         f"\nPassword:{password} \nIs it ok to save?")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
        "email":email,
        "password":password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill in your details")
    else:
        try:
            with open("data.json", "r") as data_file:
            #Reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open ("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving update data
                json.dump(data,data_file,indent=4)
            # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
            #                         f"\nPassword:{password} \nIs it ok to save?")
            
            # if is_ok:
            #     with open("data.json", "w") as data_file:
            #         data_file.write(f"{website} | {email} | {password}\n")
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height= 200)
mypass_img = PhotoImage(file="day_29_password/logo.png")
canvas.create_image(100,100, image = mypass_img)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column =0,row = 1 )
username_label = Label(text="Email/Username:")
username_label.grid(column =0,row =2, )
password_label = Label(text="Password")
password_label.grid(row=3, column = 0,)


#Entries
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.insert(0,"ocomilj@gmail.com")
email_entry.grid(row=2, column=1)
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)

#buttons
gen_pass_button = Button(text="Generate Password", command=generate_pas)
gen_pass_button.grid(row= 3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row= 1, column=2)

window.mainloop()