from tkinter import*
import pandas 
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("day_31_Capstone_FlashCards/data/Words_to_learn.csv")
except FileNotFoundError:
    original_data =  pandas.read_csv("day_31_Capstone_FlashCards/data/french_words.csv")
    to_learn =  original_data.to_dict(orient="records")
else:
    to_learn =  data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn) 
    current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text= current_card["French"])
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("day_31_Capstone_FlashCards/data/Words_to_learn", index=FALSE)





def flip_card():
    
    canvas.itemconfig(canvas_fb, image =card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")
    



window = Tk()
window.title("Flashy")
flip_timer = window.after(3000, func=flip_card)
# window.minsize(width=600,height=600)
window.config(padx=50,pady=10 , background=BACKGROUND_COLOR)


canvas = Canvas(width=900 , height=700, bg= BACKGROUND_COLOR, highlightthickness=0)
#frontcard
card_front = PhotoImage(file="day_31_Capstone_FlashCards/images/card_front.png")
card_back = PhotoImage(file="day_31_Capstone_FlashCards/images/card_back.png")
canvas_fb = canvas.create_image(450,280, image = card_front)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40 , "italic"))
card_word = canvas.create_text(450,350, text="", font=("Ariel", 60 , "bold"))
canvas.grid(column=0,row=0, columnspan=2)

right_image = PhotoImage(file="day_31_Capstone_FlashCards/images/right.png")
know_button = Button(image=right_image,highlightthickness=0, command=is_known)
know_button.grid(column=0,row=1)
#wrong
wrong_image = PhotoImage(file="day_31_Capstone_FlashCards/images/wrong.png")
unknow_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
unknow_button.grid(column=1,row=1)




next_card()

window.mainloop()
