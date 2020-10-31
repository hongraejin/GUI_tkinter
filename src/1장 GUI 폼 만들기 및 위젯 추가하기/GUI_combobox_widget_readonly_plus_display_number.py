import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("ComboBox Widget")

a_label = ttk.Label(win, text='Enter a name :')
a_label.grid(column=0, row=0)

# Button Click Event
def click_me():
    action.configure(text="I have been Clicked : "+name.get()+" "+number_chosen.get())

# Textbox Entry
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0,row=1)

# 버튼
action = ttk.Button(win, text='Click Me', command=click_me)
action.grid(column=3, row=1)

# 콥보박스위의 라벨
ttk.Label(text='Choose one of numbers').grid(column=1,row=1)


# 콤보박스 만들기
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1,2,3,4,5)
number_chosen.grid(column=2, row=1)
number_chosen.current(1)

name_entered.focus()

win.mainloop()