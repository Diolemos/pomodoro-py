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

timer = None
timer_text = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text,text='00:00') 
    # timer_text.config(text="00:00")
    #title_lable "Timer"
    title_label.config(text="Timer",fg=GREEN)
    #reset check_marks
    check_marks.config(text="")
    global session
    session = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
session = 0


def start_timer():
    global session
    session += 1
    
    if session == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
        
    
    elif session % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work",fg=GREEN)
        
    
    else:
        count_down(SHORT_BREAK_MIN * 60)  
        title_label.config(text="Break",fg=PINK) 
           
    
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()   
        mark = ''
        global session
        work_sessions = math.floor(session/2)  
        for _ in range(work_sessions):
            mark += "✔"
            check_marks.config(text=mark)  

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)




title_label = Label(text='Timer', fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", font=(FONT_NAME,35,"bold"), fill='white')
canvas.grid(column=1,row=1)




start_btn = Button(text="start",command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="reset",command=reset_timer)
reset_btn.grid(row=2,column=2)

check_marks = Label( fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()
