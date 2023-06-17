from tkinter import *
from tkinter import messagebox
import os

def signup():
    sign_up = Toplevel()
    sign_up.title("Sign UP")
    sign_up.geometry("400x250")
    sign_up.config(bg='#1a1a1a')

    def check():
        path = "E:\Scripts\programes\MRUH\App_dev\Game_Hub\main\data\ "
        if len(username.get()) == 0 or len(password.get()) == 0:
            messagebox.showerror("Error", "Please fill the username and password boxes.")
        if password.get() != rpassword.get():
            messagebox.showerror("Error", "Password does not match.")
        else:
            if os.path.isdir(path) and os.path.isfile(path+username.get()):
                data = open("Documents\gamehub\data\ "+username.get(), "w")
                datalines = [username.get()+"\n", password.get()]
                data.writelines(datalines)
                data.close()
            elif os.path.isdir(path) or os.path.isfile(path+username.get()):
                data = open(path+username.get(), "x")
                datalines = [username.get()+"\n", password.get()]
                data.writelines(datalines)
                data.close()
            else:
                os.mkdir(path)
                data = open(path+username.get(), "x")
                datalines = [username.get()+"\n", password.get()]
                data.writelines(datalines)
                data.close()

            sign_up.destroy()


    password = StringVar()
    rpassword = StringVar()
    username = StringVar()


    u_name = Label(sign_up, text="USERNAME", bg="#1a1a1a", fg="white").place(x = 30,y = 50)
    e_name = Entry(sign_up, bg="#1a1a1a", fg="white", textvariable=username).place(x = 100, y = 50)
    u_passwd = Label(sign_up, text="PASSWORD", bg="#1a1a1a", fg="white").place(x = 30, y = 90)
    e_passwd = Entry(sign_up,bg="#1a1a1a", fg="white", textvariable=password, show = "*").place(x = 100, y = 90)
    u_passwdr = Label(sign_up, text="CONFIRM \nPASSWORD", bg="#1a1a1a", fg="white").place(x = 30, y = 130)
    e_passwdr = Entry(sign_up, bg="#1a1a1a", fg="white", textvariable=rpassword, show = "*").place(x = 100, y = 130)
    submit = Button(sign_up, bg="#1a1a1a", fg="white", text="Submit", command=check).place(x = 100, y = 180)


    sign_up.mainloop()

if __name__ == "__main__":
    signup()
