from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = " "
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    # if reps < 4:
    #      count_down(work_sec)
    #      count_down(short_break_sec)
    #      reps += 1
         
    # else:
    #     count_down(long_break_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer =window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark +=  "✓"
        tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day_28_pomodoro/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


timer_label = Label(text="Timer" ,fg=GREEN,bg=YELLOW, font=(FONT_NAME,33) )
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0,row=2)
resert_button = Button(text="Reset", command=reset_timer)
resert_button.grid(column=2,row=2)

tick_label = Label( bg=YELLOW,fg=GREEN)
tick_label.grid(column="1", row="3")


window.mainloop()