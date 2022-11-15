# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from compars import Database

# db
db = Database("compars")

# Page layout
compound = Tk()
compound.title("LOGIN")
compound.geometry("900x600+0+0")
compound.config(bg="#2c3e50")

ent_frame = Frame(compound, bg="#2c3e50")
ent_frame.pack(side=TOP, fill=X)

# Title layout
title = Label(ent_frame, text=" COMPUNDS ", font=("monaco", 32), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=4, padx=250, pady=40)


# Database into there
def funl():
    maxl = db.sqlcountl()
    global a
    a = maxl


def fund():
    maxd = db.sqlcountd()
    global b
    b = maxd


def funw():
    maxw = db.sqlcountw()
    global c
    c = maxw


funl()
fund()
funw()

# Label show of db
labell = Label(ent_frame, text='            Animal Display Area – Live Streaming ', font=("calibri", 28, "bold"),
               bg="#2c3e50", fg="white")
labell.grid(row=1, column=2, padx=10, pady=10)

labell = Label(ent_frame, text='LION SLOT COUNT : ' + str(a), font=("calibri", 18, "bold"), bg="#2c3e50", fg="white")
labell.grid(row=2, column=2, padx=10, pady=10)

labeld = Label(ent_frame, text='DEAR SLOT COUNT : ' + str(b), font=("calibri", 18, "bold"), bg="#2c3e50", fg="white")
labeld.grid(row=3, column=2, padx=10, pady=10)

labelw = Label(ent_frame, text='WOLF SLOT COUNT : ' + str(c), font=("calibri", 18, "bold"), bg="#2c3e50", fg="white")
labelw.grid(row=4, column=2, padx=10, pady=10)


# Next page
def loginnext():
    compound.destroy()
    import main


# Last page
def tree():
    compound.destroy()
    import comtree


# Page btn
btn_frame = Frame(ent_frame, bg="#2c3e50")
btn_frame.grid(row=6, columnspan=4, padx=10, pady=10)

btn_tree = Button(btn_frame, command=tree, text="VIEW COMPARS", font=("calibri", 12, "bold"), bg="white",
                  fg="dodgerblue4", bd=0)
btn_tree.grid(row=0, column=2, padx=10, pady=10)

btn_main = Button(btn_frame, command=loginnext, text="ADD COMPARS", font=("calibri", 12, "bold"), bg="white",
                  fg="dodgerblue4", bd=0)
btn_main.grid(row=0, column=1, padx=10, pady=10)

compound.mainloop()
