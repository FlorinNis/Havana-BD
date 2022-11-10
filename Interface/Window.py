from tkinter import *
from tkinter import messagebox

window = Tk()
newWindow = Tk()
newWindow.withdraw()

def loginWindow():
    window.title("Havana Bar")
    window.geometry("500x500")
    #window.configure(width=500, height=500)
    window.configure(bg='lightgrey')

    login()
    window.mainloop()

def startNewWindow():
    newWindow.iconify()
    newWindow.deiconify()

    newWindow.title("Havana Bar")
    newWindow.geometry("500x500")
    #window.configure(width=500, height=500)
    newWindow.configure(bg='lightgrey')

    havana = Label(newWindow, text="Test", font='Arial 17 bold')
    havana.place(x=150, y=100)

    newWindow.mainloop()


def validateLogin(username, password):
    print("username entered: ", username.get())
    print("password entered :", password.get())
    if username.get() == "admin" and password.get() == "admin":
        messagebox.showinfo("Succes", "Login complete")
        print("login complet")
        window.destroy()
        startNewWindow()

    else:
        messagebox.showinfo("Error", "Date incorecte")
        print("login esuat")
    return

def login():
    havana = Label(window, text="Havana Bar Login", font='Arial 17 bold')
    havana.place(x=150, y=100)

    #username
    usernameLabel = Label(window, text="User Name")
    usernameLabel.place(x=120, y=200)
    username = StringVar()
    usernameEntry = Entry(window, textvariable=username)
    usernameEntry.place(x=200, y=200);

    #password
    passwordLabel = Label(window, text="Password")
    passwordLabel.place(x=120, y=230)
    password = StringVar()
    passwordEntry = Entry(window, textvariable=password, show='*')
    passwordEntry.place(x=200, y=230)

    #validateLogin = partial(validateLogin, username, password)

    #loginButon
    loginButton = Button(window, text="Login", command=lambda: validateLogin(username, password))
    loginButton.place(x=240, y=260)