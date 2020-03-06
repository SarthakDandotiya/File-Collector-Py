# import tkinter
from tkinter import *

window = Tk()

window.title("File Collector")
# window.geometry("400x200")
window.configure(background="#3E4149", pady=20, padx=40)

# Heading
heading_TXT = Label(window, foreground="white", text="File Collector",
                    font=("Arial Bold", 24), background="#3E4149")
heading_TXT.pack()

# Input Search Directory path
input_TXT = Label(window, foreground="#BDBDBD",
                  text="Complete path of directory to search:", background="#3E4149", pady=5)
input_TXT.pack()
searchdir_INP = Entry(window, width=35)
searchdir_INP.pack()

# Input Destination Directory path
output_TXT = Label(window, foreground="#BDBDBD",
                   text="Complete path of directory to copy to:", background="#3E4149", pady=5)
output_TXT.pack()
destdir_INP = Entry(window, width=35)
destdir_INP.pack()

# Input file extension
extension_TXT = Label(window, foreground="#BDBDBD",
                      text="Copy files with the extension [without '.']:", background="#3E4149", pady=5)
extension_TXT.pack()
extension_INP = Entry(window, width=35)
extension_INP.pack()

# Run Button
run_BTN = Button(window, text="Copy Files", font=("Arial Medium", 14),
                 highlightbackground="#3E4149", background="#3E4149", foreground="#FFFFFF", pady=20, width=15)
run_BTN.pack()

# Status
status_TXT = Label(window, foreground="#BDBDBD",
                   text="Ready...", background="#3E4149")
status_TXT.pack()

window.mainloop()
