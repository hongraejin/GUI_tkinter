import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk()
win.title("Ray GUI")

def _quit():
    win.quit()
    win.destroy()
    exit()

menu_bar = Menu(win)
win.config(menu=menu_bar)
file_menu = Menu(menu_bar)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')



mighty = ttk.LabelFrame(win, text='mighty frame')
mighty.grid(column=0, row=0, padx=50, pady=40)

# 이름 입력
nameLabel = ttk.Label(mighty, text='Enter a name :')
nameLabel.grid(column=0, row=0, sticky=tk.W)
# 입력창 추가
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

# 숫자 임력
numberLabel = ttk.Label(mighty, text='Choose a number : ')
numberLabel.grid(column=1, row=0, sticky=("N","S","W","E"))
# 콥보박스
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1,2,4,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

# callback 함수는 command 로 연결되어야 하기 때문에 먼저 선언이 되어야 함
def btnCall():
    print("action btn clicked")
    action.configure(text='Clicked!')

# Click 시동작할 버튼
action = ttk.Button(mighty, text="Click me!", command=btnCall)
action.grid(column=2, row=1)


def radCall():
    print("radioCall")
    radval = radVal.get()
    print("radval : ", radval)
    # win.configure(background=)

radioBtnText = ['Disabled', 'UnChecked', 'Enabled']
is_selected = [True, False, True]
chVarDisList = [tk.IntVar() for i in range(3)]
# chVarDis = tk.IntVar()

for i in range(3):
    curChBtn = tk.Checkbutton(mighty,text=radioBtnText[i], variable=chVarDisList[i])
    curChBtn.grid(column=i, row=2, sticky=tk.W)



# 리스트로 버튼을 관리하기 위한 준비
colors = ['Blue','Gold','Red']
radVal = tk.IntVar()

# 없는 값을 set하여 예상치 못한 동작을 방지한다.
radVal.set(3)

for i,color in enumerate(colors):
    curRad = tk.Radiobutton(mighty, text=color, variable=radVal, value=i, command=radCall)
    curRad.grid(column=i, row=3, sticky=tk.W)

# Frame은 구체화 할 수 있는 Widget이 있어야 보인다.
buttons_frame = ttk.LabelFrame(mighty, text="buttons_frame")
buttons_frame.grid(column=0, row=4, padx=20, pady=40, columnspan=3)

for i in range(3):
    ttk.Label(buttons_frame, text='Label'+str(i)).grid(column=i, row=5, sticky=tk.W)

for i in range(3):
    ttk.Label(buttons_frame, text='Label'+str(i)).grid(column=3, row=i+6 , sticky=tk.W)

# Frame 내에 잇는 Widget 에 대한 padding
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# scrolledtext 는 width, height, warp 속성을 정의해준다.
scrol_w = 30
scrol_h = 3
src = scrolledtext.ScrolledText(mighty, width=scrol_w, height = scrol_h, wrap=tk.WORD)
src.grid(column=0, columnspan=3)

win.mainloop()

