from tkinter import *


def startNewWindow(newWindow):
    newWindow.iconify()
    newWindow.deiconify()

    newWindow.title("Havana Bar")
    newWindow.geometry("500x500")
    #window.configure(width=500, height=500)
    newWindow.configure(bg='lightgrey')

    havana = Label(newWindow, text="Test", font='Arial 17 bold')
    havana.place(x=150, y=100)

    newWindow.mainloop()