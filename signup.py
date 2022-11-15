# Imports
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data import Database
from tkinter.messagebox import showerror
import re

# Db
db = Database("password")

# Page layout
logins = Tk()
logins.title("zoo")
logins.geometry("900x600+0+0")
logins.config(bg="white")

ent_frame = Frame(logins, bg="white")
ent_frame.pack(side=TOP, fill=X)

# Title layout
title = Label(ent_frame, text=" ASGARD  ZOO ", font=("monaco", 32), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=3, padx=250, pady=40)

head = Label(ent_frame, text="CREATE ID", font=("calibri", 20, "bold"), bg="white", fg="black")
head.grid(row=1, columnspan=3, padx=250, pady=20)

# Set variable
name = StringVar()
dob = StringVar()
username = StringVar()
password = StringVar()
solt = StringVar()


# add data sql
def add_data():
    if txtname.get == "" or txtage.get() == "" or txtusername.get() == "" or txtpass.get() == "" or combosolt.get() == "":
        messagebox.showerror("Error in Input", "PLease Fill ALL the Data")
        return
    else:
        try:
            con = sqlite3.connect("password")
            core = con.cursor()
            sql = " select * from password where   username = '%s'"
            name = txtusername.get()
            core.execute(sql % (name))
            data = core.fetchone()
            print(data)
            if bool(data) == True:
                messagebox.showerror("Error in Input", "USER NAME Already Exists")
            else:
                db.insert(txtname.get(), txtage.get(), txtusername.get(), txtpass.get(), combosolt.get())
                messagebox.showinfo("Success", "SUCESSFULLY ID CERATE")
                clearall()
        except Exception as e:
            showerror("issue", e)


# clear all
def clearall():
    name.set("")
    dob.set("")
    username.set("")
    password.set("")
    solt.set("")


# Login page
def login():
    logins.destroy()
    import login


# Exit
def exit():
    logins.destroy()


# Signup label
lblname = Label(ent_frame, text="NAME", font=("calibri", 12, "bold"), bg="white", fg="black")
lblname.grid(row=2, column=1, padx=10, pady=10, sticky="w")
txtname = Entry(ent_frame, textvariable=name, font=("calibri", 12), bg="white", fg="black")
txtname.grid(row=2, column=2, padx=10, pady=10, sticky="w")

lblage = Label(ent_frame, text="AGE", font=("calibri", 12, "bold"), bg="white", fg="black")
lblage.grid(row=3, column=1, padx=10, pady=10, sticky="w")
txtage = Entry(ent_frame, textvariable=dob, font=("calibri", 12), bg="white", fg="black")
txtage.grid(row=3, column=2, padx=10, pady=10, sticky="w")

lblusername = Label(ent_frame, text="USERNAME", font=("calibri", 12, "bold"), bg="white", fg="black")
lblusername.grid(row=4, column=1, padx=10, pady=10, sticky="w")
txtusername = Entry(ent_frame, textvariable=username, font=("calibri", 12), bg="white", fg="black")
txtusername.grid(row=4, column=2, padx=10, pady=10, sticky="w")

lblpass = Label(ent_frame, text="PASSWORD", font=("calibri", 12, "bold"), bg="white", fg="black")
lblpass.grid(row=5, column=1, padx=10, pady=10, sticky="w")
txtpass = Entry(ent_frame, textvariable=password, font=("calibri", 12), bg="white", fg="black")
txtpass.grid(row=5, column=2, padx=10, pady=10, sticky="w")

lblsolt = Label(ent_frame, text="TYPE", font=("calibri", 12, "bold"), bg="white", fg="black")
lblsolt.grid(row=6, column=1, padx=10, pady=10, sticky="w")
combosolt = ttk.Combobox(ent_frame, textvariable=solt, font=("calibri", 12), state="readonly")
combosolt['values'] = ('ADMIN', 'USER')
combosolt.grid(row=6, column=2, padx=10, pady=10, sticky="w")

# All btn
btn_frame = Frame(ent_frame, bg="white")
btn_frame.grid(row=7, columnspan=4, padx=10, pady=10)

btn_add = Button(btn_frame, command=add_data, width=15, text="CREATE ID", font=("calibri", 12, "bold"), bg="blue",
                 fg="white", bd=0)
btn_add.grid(row=7, column=1, padx=10, pady=10, sticky="w")

btn_add = Button(btn_frame, command=login, width=15, text="LOGIN", font=("calibri", 12, "bold"), bg="blue",
                 fg="white", bd=0)
btn_add.grid(row=7, column=2, padx=10, pady=10, sticky="w")

btn_edit = Button(btn_frame, command=exit, width=15, text="EXIT", font=("Calibri", 12, "bold"), fg="white",
                  bg="blue", bd=0)
btn_edit.grid(row=7, column=0, padx=10, pady=10, sticky="w")

logins.mainloop()
