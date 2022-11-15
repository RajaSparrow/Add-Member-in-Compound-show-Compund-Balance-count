# Imports
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from compars import Database
import re
from tkinter.messagebox import showerror

# Db
db = Database("compars")

# Page layout
root = Tk()
root.title("COMPARS DETAILS")
root.geometry("900x600+0+0")
root.config(bg="#2c3e50")

entry_frame = Frame(root, bg="#2c3e50")
entry_frame.pack(side=TOP, fill=X)

# Set variable
id = StringVar()
name = StringVar()
age = StringVar()
gender = StringVar()
contact = StringVar()
address = StringVar()
solt = StringVar()

# Title layout
title = Label(entry_frame, text="COMPARS DETAILS", font=("monaco", 32), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=4, padx=200, pady=40)


# For add
def add_compars():
    if txtid.get == "" or txtname.get() == "" or txtage.get() == "" or combogender.get() == "" or txtcontact.get() == "" or txtaddress.get() == "" or combosolt.get() == "":
        messagebox.showerror("Error in Input", "PLease Fill ALL the Data")
        return
    else:
        try:
            con = sqlite3.connect("compars")
            core = con.cursor()
            sql = " select * from compars where   id = '%s'"
            name = txtid.get()
            core.execute(sql % (name))
            data = core.fetchall()
            if bool(data) == True:
                messagebox.showerror("Error in Input", "ID Already Exists")
            else:
                a = txtcontact.get()
                b = re.fullmatch('[0-9]{10}', a)
                c = txtage.get()
                d = re.fullmatch('[0-9]{2}', c)
                e = txtid.get()
                f = re.fullmatch('CCZ[0-9]{4}', e)

                if b != None and d != None and f != None:
                    db.insert(txtid.get(), txtname.get(), txtage.get(), combogender.get(), txtcontact.get(),
                              txtaddress.get(),
                              combosolt.get())
                    messagebox.showinfo("Success", "Record Inserted")
                    clearall()
                else:
                    messagebox.showerror("Error in Input", "PLease check id,age,contact ")

        except Exception as e:
            showerror("issue", e)


# All clear
def clearall():
    id.set("")
    name.set("")
    age.set("")
    gender.set("")
    contact.set("")
    address.set("")
    solt.set("")


# Next page
def tree():
    root.destroy()
    import comtree


# Main page
def compound():
    root.destroy()
    import compound


# Label for id to slot
lblid = Label(entry_frame, text="ID", font=("calibri", 12, "bold"), fg="white", bg="#2c3e50")
lblid.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtid = Entry(entry_frame, textvariable=id, font=("calibri", 12), bg="white", fg="black")
txtid.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblname = Label(entry_frame, text="NAME", font=("calibre", 12, "bold"), fg="white", bg="#2c3e50")
lblname.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtname = Entry(entry_frame, textvariable=name, font=("calibri", 12), bg="white", fg="black")
txtname.grid(row=3, column=3, padx=10, pady=10, sticky="w")

lblage = Label(entry_frame, text="AGE", font=("calibri", 12, "bold"), fg="white", bg="#2c3e50")
lblage.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtage = Entry(entry_frame, textvariable=age, font=("calibri", 12), bg="white", fg="black")
txtage.grid(row=4, column=3, padx=10, pady=10, sticky="w")

lblgender = Label(entry_frame, text="GENDER", font=("calibri", 12, "bold"), fg="white", bg="#2c3e50")
lblgender.grid(row=5, column=2, padx=10, pady=10, sticky="w")
combogender = ttk.Combobox(entry_frame, textvariable=gender, font=("calibri", 12), state="readonly")
combogender['values'] = ('Male', 'Female', 'Transgender')
combogender.grid(row=5, column=3, padx=10, pady=10, sticky="w")

lblcontact = Label(entry_frame, text="CONTACT", font=("calibri", 12, "bold"), fg="white", bg="#2c3e50")
lblcontact.grid(row=6, column=2, padx=10, pady=10, sticky="w")
txtcontact = Entry(entry_frame, textvariable=contact, font=("calibri", 12), bg="white", fg="black")
txtcontact.grid(row=6, column=3, padx=10, pady=10, sticky="w")

lbladdress = Label(entry_frame, text="ADDRESS", font=("calibri", 12, "bold"), fg="white", bg="#2c3e50")
lbladdress.grid(row=7, column=2, padx=10, pady=10, sticky="w")
txtaddress = Entry(entry_frame, textvariable=address, font=("calibri", 12), bg="white", fg="black")
txtaddress.grid(row=7, column=3, padx=10, pady=10, sticky="w")

lblsolt = Label(entry_frame, text="SOLT", font=("calibri", 12, "bold"), fg="white", bg="#2c3e50")
lblsolt.grid(row=8, column=2, padx=10, pady=10, sticky="w")
combosolt = ttk.Combobox(entry_frame, textvariable=solt, font=("calibri", 12), state="readonly")
combosolt['values'] = ('Solt-1 (LOIN)', 'Solt-2 (DEAR)', 'Solt-3 (WOLF)')
combosolt.grid(row=8, column=3, padx=10, pady=10, sticky="w")

# all btn
btn_frame = Frame(entry_frame, bg="#2c3e50")
btn_frame.grid(row=9, column=1, columnspan=4, padx=10, pady=30, sticky="w")

btn_add = Button(btn_frame, command=add_compars, text="ADD DETAILS", width=15, font=("calibri", 10, "bold"), bg="white",
                 fg="dodgerblue4", bd=0)
btn_add.grid(row=0, column=2, padx=10, pady=10, sticky="w")

btn_clear = Button(btn_frame, command=clearall, text="CLEAR DETAILS", width=15, font=("Calibri", 10, "bold"),
                   bg="white", fg="dodgerblue4", bd=0)
btn_clear.grid(row=0, column=4, padx=10, pady=10, sticky="w")

btn_tree = Button(btn_frame, command=tree, text="VIEW COMPARS ", width=15, font=("calibri", 10, "bold"), bg="white",
                  fg="dodgerblue4", bd=0)
btn_tree.grid(row=0, column=5, padx=10, pady=10)

btn_compound = Button(btn_frame, command=compound, text=" VIEW COMPOUND", width=15, font=("calibri", 10, "bold"),
                      bg="white", fg="dodgerblue4", bd=0)
btn_compound.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
