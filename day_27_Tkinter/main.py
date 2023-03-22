from tkinter import *


def calculation():
    
    miles = float(miles_input.get())
    km = miles*1.609
    answer_label.config(text=f"{km}")
    

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width= 200, height=200)



#Label

equal_to_label = Label(text="Is equal to ", font=("Ariel", 10,) )
equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Ariel", 10,) )
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Ariel", 10,) )
km_label.grid(column=3, row=1)

answer_label = Label( )
answer_label.grid(column=1, row=1)


#button
button = Button(text="Calculate", command=calculation)
button.grid(column=1, row=2)


#Entry
miles_input = Entry(width=7,)
miles_input.grid(column=1,row=0)



window.mainloop()