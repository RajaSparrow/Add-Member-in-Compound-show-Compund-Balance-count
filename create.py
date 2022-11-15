#Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from compars import Database

# from PIL import ImageTk , Image

# Page layout
logins = Tk()
logins.title("zoo")
logins.geometry("900x600+0+0")
logins.config(bg="white")

ent_frame = Frame(logins, bg="white")
ent_frame.pack(side=TOP, fill=X)

# Title layout
title = Label(ent_frame, text=" ASGARD  ZOO ", font=("calibri", 42, "bold"), fg="white", bg="orange")
title.grid(row=0, columnspan=4, padx=150, pady=40)

head = Label(ent_frame, text="WELCOME TO ASGARD ZOO", font=("monaco", 32), bg="#2c3e50", fg="white")
head.grid(row=1, columnspan=4, padx=150, pady=20)


# img = ImageTk.PhotoImage(Image.open("zoo.jpg"))
# head = Label(ent_frame, image=img)
# head.grid(row=2, columnspan=4, padx=260, pady=20)

# login page
def login():
    logins.destroy()
    import login


# signup page
def signup():
    logins.destroy()
    import signup


# Exit
def exit():
    logins.destroy()


# contact
def con():
    messagebox.showinfo("CONTACT", "+ 91 ***** *****")


# all btn
btn_frame = Frame(ent_frame, bg="white")
btn_frame.grid(row=4, columnspan=4, padx=10, pady=10)

btn_add = Button(btn_frame, command=login, width=15, text="LOGIN", font=("calibri", 12, "bold"), bg="blue",
                 fg="white", bd=0)
btn_add.grid(row=1, column=2, padx=10, pady=10, sticky="w")

btn_edit = Button(btn_frame, command=signup, width=15, text="SIGN UP", font=("Calibri", 12, "bold"), fg="white",
                  bg="blue", bd=0)
btn_edit.grid(row=2, column=2, padx=10, pady=10, sticky="w")

btn_edit = Button(btn_frame, command=con, width=15, text="CONTACT US", font=("Calibri", 12, "bold"), fg="white",
                  bg="blue", bd=0)
btn_edit.grid(row=4, column=2, padx=10, pady=10, sticky="w")

btn_edit = Button(btn_frame, command=exit, width=15, text="EXIT", font=("Calibri", 12, "bold"), fg="white",
                  bg="blue", bd=0)
btn_edit.grid(row=3, column=2, padx=10, pady=10, sticky="w")

logins.mainloop()
