from tkinter import *
def func():
    def autologin():
        username.set("Ritesh")
        password.set("*****")
    login_screen = Tk()
    login_screen.title("Autologin with python")
    login_screen.geometry("300x250")

    Label(login_screen, Text="Username").pack()
    username = StringVar()
    password = StringVar()
    username_login_entry = Entry(login_screen, textvariable=username)
    username_login_entry.pack()

    Label(login_screen, Text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password)
    password_login_entry.pack()

    Button(login_screen, Text="Apply autofill", command=autologin).pack()
    Button(login_screen, Text="login Now", width=10, height=1).pack(pady=10)

    login_screen.mainloop()

func()