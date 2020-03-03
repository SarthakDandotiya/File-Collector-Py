# import tkinter
from tkinter import *

window = Tk()

window.title("File Collector")
window.geometry("350x200")
window.configure(background="#3E4149")

lbl = Label(window, foreground="white", text="Hello",
            font=("Arial Bold", 24), background="#3E4149")
lbl.grid(row=0, column=0)

window.mainloop()
