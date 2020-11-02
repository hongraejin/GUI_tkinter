import tkinter as tk
from tkinter import ttk

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

# 라디오 버튼에 활용될 글로벌 변수
colors = ['Blue',"Gold","Red"]

# 라디오 버튼이 눌릴때마다 호출될 callback 함수
def radCall():
    action.configure(background=colors[radVar.get()])

# 라디오 버튼에 활용할 정수 변수를 선언한다.
radVar = tk.IntVar()

# 사용되지 않을 인덱스를 선택해서, 오류를 방지한다.
radVar.set(3)

for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

win.mainloop()