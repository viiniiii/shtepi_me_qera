import tkinter
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
CHECK = "✓"
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    sahati.config(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
    canvas.itemconfig(timer_value,text="00:00")
    checks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        sahati.config(text="Break",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        sahati.config(text="Break",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
        count_down(SHORT_BREAK_MIN*60)

    else:
        sahati.config(text="Work",fg=RED,bg=YELLOW,font=(FONT_NAME,45,"bold"))
        count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_value,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer 
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        for i in range(0,math.floor(reps/2)):
            marks += "✓"
        checks.config(text=marks) 
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title("Pomodoro")

sahati = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
sahati.grid(row=0,column=1)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="pomodoro\domate.png")
canvas.create_image(100,112,image=tomato_img)
timer_value = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start = tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)

reset = tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

checks = tkinter.Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,15,"bold"))
checks.grid(row=3,column=1)
window.mainloop()