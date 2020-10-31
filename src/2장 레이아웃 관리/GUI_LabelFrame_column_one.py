import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title("Raymond Application")

buttons_frame = ttk.LabelFrame(win, text="Labels in a Frame")
buttons_frame.grid(column=0, row=0)

for i in range(3):
    ttk.Label(buttons_frame, text='Label'+str(i)).grid(column=i, row=0, sticky=tk.W)

for i in range(3):
    ttk.Label(buttons_frame, text='Label'+str(i)).grid(column=3, row=i , sticky=tk.W)


win.mainloop()