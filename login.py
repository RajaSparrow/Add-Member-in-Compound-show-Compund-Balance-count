# Imports
import sqlite3 as sql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from compars import Database

# Page layout
login = Tk()
login.title("LOGIN")
login.geometry("900x600+0+0")
login.config(bg="white")

ent_frame = Frame(login, bg="white")
ent_frame.pack(side=TOP, fill=X)

# Set variable
loginid = StringVar()
passworda = StringVar()

# Title layout
title = Label(ent_frame, text=" ASGARD  ZOO ", font=("monaco", 32), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=4, padx=250, pady=40)

head = Label(ent_frame, text="LOGIN", font=("calibri", 24, "bold"), bg="white", fg="black")
head.grid(row=1, columnspan=4, padx=260, pady=20)


# Password & next page
def loginnext():
    username = txtname.get()
    password = txtpass.get()
    solt = combosolt.get()
    con = sql.connect("password")
    cur = con.cursor()
    statement = f"SELECT username from password WHERE username='{username}' AND Password = '{password}' AND solt = '{solt}';"
    cur.execute(statement)
    if not cur.fetchone():
        messagebox.showerror("Error in Input", "USERNAME OR PASSWORD INCORRECT")
    else:
        if solt == "ADMIN":
            login.destroy()
            import compound
        else:
            login.destroy()
            import main2


# clearall
def clearall():
    loginid.set("")
    passworda.set("")


# Login label
lblname = Label(ent_frame, text="USERNAME", font=("calibri", 12, "bold"), bg="white", fg="black")
lblname.grid(row=2, column=1, padx=10, pady=10, sticky="e")
txtname = Entry(ent_frame, textvariable=loginid, font=("calibri", 12), bg="white", fg="black")
txtname.grid(row=2, column=2, padx=10, pady=10, sticky="w")

lblpass = Label(ent_frame, text="PASSWORD", font=("calibri", 12, "bold"), bg="white", fg="black")
lblpass.grid(row=3, column=1, padx=10, pady=10, sticky="e")
txtpass = Entry(ent_frame, textvariable=passworda, font=("calibri", 12), bg="white", fg="black")
txtpass.grid(row=3, column=2, padx=10, pady=10, sticky="w")

lblsolt = Label(ent_frame, text="TYPE", font=("calibri", 12, "bold"), bg="white", fg="black")
lblsolt.grid(row=4, column=1, padx=10, pady=10, sticky="e")
combosolt = ttk.Combobox(ent_frame, font=("calibri", 12), state="readonly")
combosolt['values'] = ('ADMIN', 'USER')
combosolt.grid(row=4, column=2, padx=10, pady=10, sticky="w")

# Login btn
btn_frame = Frame(ent_frame, bg="white")
btn_frame.grid(row=5, columnspan=4, padx=10, pady=10)

btn_login = Button(btn_frame, command=loginnext, text="   LOGIN   ", font=("calibri", 12, "bold"), fg="white",
                   bg="blue", bd=0)
btn_login.grid(row=0, column=1, padx=10, pady=10)

login.mainloop()
