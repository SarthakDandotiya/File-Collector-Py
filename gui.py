# import tkinter
from tkinter import *

window = Tk()

window.title("File Collector")
window.geometry("300x100")
window.configure(background="#3E4149", pady=10, padx=20)

# Heading
heading_TXT = Label(window, foreground="white", text="File Collector",
                    font=("Arial Bold", 24), background="#3E4149")
heading_TXT.pack()

# Search Folder
search_BTN = Button(window, text="Search Folder",
                    highlightbackground="#3E4149", background="#3E4149", foreground="#FFFFFF")
search_BTN.pack()


window.mainloop()
