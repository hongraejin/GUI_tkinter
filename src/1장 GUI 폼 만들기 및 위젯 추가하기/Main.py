import tkinter as tk
from tkinter import ttk
from datetime import datetime

now_str = datetime.now().strftime("%Y-%m-%d")

def start_btn():
    print("시작버튼 클릭")
    action.configure(text="버튼이 눌렸습니다.")
    # a_

win = tk.Tk()
win.title("맛집탐방.Ver2")

a_label = ttk.Label(win, text=now_str)
a_label.grid(column=0, row=0)

action = ttk.Button(win, text="시작", command=start_btn)
action.grid(column=1, row=0)



win.mainloop()