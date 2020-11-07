import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Raymond GUI Tab")

# tab 담기위한 tabControl ①
tabControl = ttk.Notebook(win) #

# tab1, tab2 생성
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')

# tab1 Frame 만들고 위젯 포함 ②
mighty = ttk.LabelFrame(tab1, text='tab1 content')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Frame 에 구체적인 widget 포함 ③
a_label = ttk.Label(mighty, text='Enter a name : ')
a_label.grid(column=0, row=0, sticky='W')

# tab2 Frame 만들고 위젯 포함 ②
tab2_mighty = ttk.LabelFrame(tab2, text='tab2 content')
tab2_mighty.grid(column=0, row=0 , padx=8, pady=4)

# Frame 에 구체적인 widget 포함 (반복문) ③
radioBtnText = ['Disabled', 'UnChecked', 'Enabled']
is_selected = [True, False, True]
chVarDisList = [tk.IntVar() for i in range(3)]
# chVarDis = tk.IntVar()

for i in range(3):
    curChBtn = tk.Checkbutton(tab2_mighty,text=radioBtnText[i], variable=chVarDisList[i])
    curChBtn.grid(column=i, row=2, sticky=tk.W)

win.mainloop()
