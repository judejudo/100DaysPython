from tkinter import *
from tkinter import messagebox
def click():
    while(True):
        messagebox.askretrycancel(title="pro",message="are you good ")

    
window=Tk()
button=Button(command=click ,text="i love you")
button.pack()
window.mainloop()