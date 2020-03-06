# import tkinter
from tkinter import *
from commands import copyFiles

window = Tk()

window.title("File Collector")
window.configure(background="#3E4149", pady=20, padx=40)

# UI Functions ->

origin = ''
destination = ''
extension = ''


def clicked():

    origin = searchdir_INPUT.get()
    destination = destdir_INPUT.get()
    extension = extension_INPUT.get()

    copyFiles(origin, destination, extension)

    complete()


def complete():
    status_LABEL.configure(text="Done.")

# UI Layout ->

    # Heading
heading_LABEL = Label(window, foreground="white", text="File Collector",
                      font=("Arial Bold", 24), background="#3E4149")
heading_LABEL.pack()

# Input Search Directory path
input_LABEL = Label(window, foreground="#BDBDBD",
                    text="Complete path of directory to search:", background="#3E4149", pady=5)
input_LABEL.pack()
searchdir_INPUT = Entry(window, width=35)
searchdir_INPUT.pack()

# Input Destination Directory path
output_LABEL = Label(window, foreground="#BDBDBD",
                     text="Complete path of directory to copy to:", background="#3E4149", pady=5)
output_LABEL.pack()
destdir_INPUT = Entry(window, width=35)
destdir_INPUT.pack()

# Input file extension
extension_LABEL = Label(window, foreground="#BDBDBD",
                        text="Copy files with the extension [without '.']:", background="#3E4149", pady=5)
extension_LABEL.pack()
extension_INPUT = Entry(window, width=35)
extension_INPUT.pack()

# Run Button
run_BUTTON = Button(window, text="Copy Files", command=clicked, font=("Arial Medium", 14),
                    highlightbackground="#3E4149", background="#3E4149", foreground="#FFFFFF", pady=20, width=15)
run_BUTTON.pack()

# Status
status_LABEL = Label(window, foreground="#BDBDBD",
                     text="Ready...", background="#3E4149")
status_LABEL.pack()

window.mainloop()
