import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Raymond GUI Tab")

tabControl = ttk.Notebook(win) #
tab1 = ttk.Frame(tabControl) # Frame 함수의 인자로 tabControl 이 들어가니까, 이곳에 소속된것을 예측해야함
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill='both')

win.mainloop()
