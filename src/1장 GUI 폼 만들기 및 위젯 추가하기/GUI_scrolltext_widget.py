import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
# 윈도우 생성 on Memory
win = tk.Tk()
win.title("ComboBox Widget")


# Entry 위 라벨
a_label = ttk.Label(win, text='Enter a name :')
a_label.grid(column=0, row=0)

# 콤보박스위의 라벨
ttk.Label(text='Choose one of numbers').grid(column=1,row=0)

# Textbox Entry
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0,row=1)
name_entered.focus()


# Button Click Event
def click_me():
    action.configure(text="I have been Clicked : "+name.get())

# 버튼
action = ttk.Button(win, text='Click Me', command=click_me)
action.grid(column=2, row=1)


# 콤보박스 만들기
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1,2,3,4,5)
number_chosen.grid(column=1, row=1)
number_chosen.current(1)


# CheckButton 만들기
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled',variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=3, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=3, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=3, sticky=tk.W)

# Radiobutton Globals
COLOR1 = 'Blue'
COLOR2 = "Gold"
COLOR3 = "Red"

# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if radSel == 1 : win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3 : win.configure(background=COLOR3)

# creat three Radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text= COLOR1 , variable = radVar, value =1 , command = radCall)
rad1.grid(column=0 , row= 4, sticky = tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text= COLOR2 , variable = radVar, value = 2 , command = radCall)
rad2.grid(column=1 , row= 4, sticky = tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text= COLOR3, variable = radVar, value = 3, command = radCall)
rad3.grid(column=2 , row= 4, sticky = tk.W, columnspan=3)

# scrolltext
scroll_w = 30
scroll_h = 3
src = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
src.grid(column=0,  columnspan=3)  # row=5 는 생략



win.mainloop()


