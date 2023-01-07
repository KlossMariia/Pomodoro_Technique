from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
reps = 0
checkmark_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer, reps, checkmark_text
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", foreground=GREEN)
    checkmark_text = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps != 0:
        window.after_cancel(timer)
    reps += 1
    if reps % 8 == 0:
        time = LONG_BREAK_SEC
        title_label.config(text="Long Break!")
        reps = 0
    elif reps % 2 == 0:
        time = SHORT_BREAK_SEC
        title_label.config(text="Short Break!")
    else:
        time = WORK_SEC
        title_label.config(text="Work!", foreground=RED)
    countdown(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps != 0 and reps % 2 == 0:
            global checkmark_text
            checkmark_text += "✓"
            checkmark_label.config(text=checkmark_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Creating labels
title_label = Label(text="Timer", font=(FONT_NAME, 35, "normal"), foreground=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
checkmark_label = Label(text=checkmark_text, font=(FONT_NAME, 30, "normal"), foreground=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# Creating Buttons
start_button = Button(text="Start", command=start_timer, height=2, width=5, highlightthickness=0, borderwidth=0,
                      bg=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, height=2, width=5, highlightthickness=0, borderwidth=0,
                      bg=YELLOW)
reset_button.grid(column=2, row=2)


window.mainloop()