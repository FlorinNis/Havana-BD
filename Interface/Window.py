from tkinter import *
from functools import partial
from tkinter import messagebox

window = Tk()

def startWindow():
    window.title("Havana Bar")
    window.configure(width=500, height=500)
    window.configure(bg='lightgrey')

    login()
    window.mainloop()


def validateLogin(username, password):
    print("username entered: ", username.get())
    print("password entered :", password.get())
    if username.get() == "admin" and password.get() == "admin":
        messagebox.showinfo("Succes", "Login complete")
        print("login complet")
    else:
        messagebox.showinfo("Error", "Date incorecte")
        print("login esuat")
    return

def login():
    #username
    usernameLabel = Label(window, text="User Name").grid(row = 0, column = 0)
    username = StringVar()
    usernameEntry = Entry(window, textvariable=username).grid(row=0, column =1)

    #password
    passwordLabel = Label(window, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)

    #validateLogin = partial(validateLogin, username, password)

    #loginButon
    loginButton = Button(window, text="Login", command=lambda: validateLogin(username, password)).grid(row=4, column=0)