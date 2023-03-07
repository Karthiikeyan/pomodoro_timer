from tkinter import *
import random
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
hearts = ["💚","💛","❤️","🤍","💙","🧡","💜","🖤"]
time_control = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    canvas.after_cancel(time_control)
    canvas.itemconfig(timing, text="00:00")
    timer.config(text="Timer")
    tick_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_count():
    global reps
    reps +=1

    if reps % 8 ==0:
        timer.config(text="Break", font=(FONT_NAME,40,"bold"), fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", font=(FONT_NAME, 50,"bold"), fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minute = math.floor(count/60)
    second = count % 60

    if second < 10:
        second = f"0{second}"

    if count > 0:
        global time_control
        canvas.itemconfig(timing, text=f"{minute}:{second}")
        time_control = canvas.after(1000, count_down, count-1)
    else:
        start_count()
        work = math.floor(reps/2)
        mark = ""
        for _ in range(work):
            mark += random.choice(hearts)
        tick_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(500,500)
window.maxsize(600,600)
window.config(padx=100,pady=100, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME,50,"bold"), foreground=GREEN, bg=YELLOW, highlightthickness=0)
timer.config(pady=10, padx=10)
timer.grid(row=0,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timing = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1,column=1)
# canvas.pack()

start = Button(text="start", width=7, highlightthickness=0, command=start_count)
start.grid(row=2, column=0)

reset = Button(text="Reset", width=7, highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

tick = "✔"
tick_mark = Label(text="", bg=YELLOW, highlightthickness=0)
tick_mark.grid(row=3, column=1)






window.mainloop()


