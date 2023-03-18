from tkinter import *

window = Tk()

window.title("My Fist GUI Program")
window.minsize(width= 500, height=300)


#Label

my_label = Label(text="I am a label", font=("Ariel", 24,"italic") )
my_label.pack()


def button_clicked():
    print("I have been clicked")
    word = input.get()
    my_label.config(text = word)

button = Button(text="Click Me", command=button_clicked)
button.pack()



#Entry

input = Entry(width=10,)
entry.insert(END, string="Some text to begin with.")
input.pack()






window.mainloop()