import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Raymond Application")

# 이름 입력
ttk.Label(win, text='Enter a name :').grid(column=0, row=0)
# 입력창 추가
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

# 숫자 임력
ttk.Label(win, text='Choose a number : ').grid(column=1, row=0)
# 콥보박스
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1,2,4,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

# callback 함수는 command 로 연결되어야 하기 때문에 먼저 선언이 되어야 함
def btnCall():
    print("action btn clicked")
    action.configure(text='Clicked!')

# Click 시동작할 버튼
action = ttk.Button(win, text="Click me!", command=btnCall)
action.grid(column=2, row=1)


def radCall():
    print("radioCall")
    radval = radVal.get()
    print("radval : ", radval)
    # win.configure(background=)

radioBtnText = ['Disabled', 'UnChecked', 'Enabled']
is_selected = [True, False, True]
chVarDis = tk.IntVar()

# for i in range(3):
#     tk.Checkbutton(win,text)



# 리스트로 버튼을 관리하기 위한 준비
colors = ['Blue','Gold','Red']
radVal = tk.IntVar()

# 없는 값을 set하여 예상치 못한 동작을 방지한다.
radVal.set(3)

for i,color in enumerate(colors):
    curRad = tk.Radiobutton(win, text=color, variable=radVal, value=i, command=radCall)
    curRad.grid(column=i, row=2, sticky=tk.W)

# Frame은 구체화 할 수 있는 Widget이 있어야 보인다.
buttons_frame = ttk.LabelFrame(win, text="Frame")
buttons_frame.grid(column=0, row=3, padx=20, pady=40, columnspan=3)

for i in range(3):
    ttk.Label(buttons_frame, text='Label'+str(i)).grid(column=i, row=4, sticky=tk.W)

for i in range(3):
    ttk.Label(buttons_frame, text='Label'+str(i)).grid(column=3, row=i+5 , sticky=tk.W)

# Frame 내에 잇는 Widget 에 대한 padding
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# scrolledtext 는 width, height, warp 속성을 정의해준다.
scrol_w = 30
scrol_h = 3
src = scrolledtext.ScrolledText(win, width=scrol_w, height = scrol_h, wrap=tk.WORD)
src.grid(column=0, columnspan=3)



win.mainloop()