from tkinter import *
from tkinter import messagebox
import os

def signin():
    sign_in = Toplevel()
    sign_in.title("Sign In")
    sign_in.geometry("400x250")
    sign_in.config(bg='#1a1a1a')

    def check():
        path = "E:\Scripts\programes\MRUH\App_dev\Game_Hub\main\data\ "
        if len(username.get()) == 0 or len(password.get()) == 0:
            messagebox.showerror("Error", "Please fill the username and password boxes.")
        if os.path.isfile(path+username.get()):
            with open(path+username.get()) as file:
                for line in file:
                    pass
                last_line = line
                if last_line == password.get():
                    messagebox.showinfo("Success", "Login successful!")
                else:
                    messagebox.showerror("Error", "Password does not match.")
        else:
            messagebox.showerror("Error", "Username not found.")

        sign_in.destroy()


    username = StringVar()
    password = StringVar()

    u_name = Label(sign_in, text="USERNAME", bg='#1a1a1a', fg='white').place(x = 30, y = 50)
    e_name = Entry(sign_in, bg='#1a1a1a', fg='white', textvariable=username).place(x = 100, y = 50)
    u_passwrd = Label(sign_in, text="PASSWORD", bg='#1a1a1a', fg='white').place(x = 30, y = 90)
    e_passwd = Entry(sign_in,bg="#1a1a1a", fg="white", textvariable=password, show = "*").place(x = 100, y = 90)
    submit = Button(sign_in, bg="#1a1a1a", fg="white", text="Submit", command=check).place(x = 100, y = 180)
    sign_in.mainloop()

if __name__ == "__main__":
    signin()
