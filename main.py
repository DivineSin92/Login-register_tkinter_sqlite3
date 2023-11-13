import tkinter as tk
from tkinter import *
from tkinter import messagebox

##############

Window = Tk()

Window.title('Title')
Window.geometry('300x400')

##############

def Login_chose():
    Chose.destroy()
    Login.pack(fill = 'both', expand = True)

def Register_chose():
    Chose.destroy()
    Register.pack(fill = 'both', expand = True)

def Login_b():
    if Login_entry.get() == 'login1' and Passwd_entry.get() == '123':
        Login.destroy()
    else:
        messagebox.showerror('Wrong', 'Wrong Login or Password')

def Login_b_e(e):
    if Login_entry.get() == 'login1' and Passwd_entry.get() == '123':
        Login.destroy()
    else:
        messagebox.showerror('Wrong', 'Wrong Login or Password')

def Clear(e):
    if Login_entry.get() == 'Login' or Passwd_entry.get() == 'Password':
        Login_entry.delete(0, END)
        Passwd_entry.delete(0, END)
        Passwd_entry.config(show = '*')

##############

Chose = Canvas(Window, width = 300, height = 400, bd = 0)

Login_c_b = Button(Window, text = 'LOGIN', width = 20, command = Login_chose)
Login_c_b_w = Chose.create_window(75, 150, anchor = 'nw', window = Login_c_b)

Register_c_b = Button(Window, text = 'REGISTER', width = 20, command = Register_chose)
Register_c_b_w = Chose.create_window(75, 250, anchor = 'nw', window = Register_c_b)

Chose.pack(fill = 'both', expand = True)

##############

Login = Canvas(Window, width = 300, height = 400, bd = 0)

Login_entry = Entry(Window, width = 30, fg = 'black', bd = 0)
Passwd_entry = Entry(Window, width = 30, fg = 'black', bd = 0)

Login_entry.insert(0, 'Login')
Passwd_entry.insert(0, 'Password')

Login_window = Login.create_window(55, 200, anchor = 'nw', window = Login_entry)
Passwd_window = Login.create_window(55, 250, anchor = 'nw', window = Passwd_entry)

Login_entry.bind('<Return>', Login_b_e)
Passwd_entry.bind('<Return>', Login_b_e)

Login_entry.bind('<Button-1>', Clear)
Passwd_entry.bind('<Button-1>', Clear)

Login_button = Button(Window, text = 'LOGIN', width = 20, command = Login_b)
Login_window = Login.create_window(55, 300, anchor = 'nw', window = Login_button)

##############

Register = Canvas(Window, width = 300, height = 400, bd = 0)

##############

Window.mainloop()
