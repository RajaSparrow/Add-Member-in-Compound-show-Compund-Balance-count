# Imports
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror
from compars import Database

# Db
db = Database("compars")

# Page layout
root = Tk()
root.title("COMPARS DATABASE")
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
title = Label(entry_frame, text="COMPARS DATABASE", font=("monaco", 32), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=5, padx=230, pady=40)


# click get data
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    gender.set(row[3])
    contact.set(row[4])
    address.set(row[5])
    solt.set(row[6])


# del
def delete_compars():
    db.delete(row[0])
    messagebox.showinfo("DELETE", "Delete Id")
    displayall()


# display
def displayall():
    tv.delete(*tv.get_children())
    for row in db.select():
        tv.insert("", END, values=row)


# update
def update_compars():
    if txtname.get() == "" or txtage.get() == "" or combogender.get() == "" or txtcontact.get() == "" or txtaddress.get() == "" or combosolt.get() == "":
        messagebox.showerror("Error in Input", "PLease Fill ALL the Data")
        return
    db.update(row[0], txtname.get(), txtage.get(), combogender.get(),
              txtcontact.get(), txtaddress.get(), combosolt.get())
    messagebox.showinfo("Success", "Record Updated")
    cleartheall()
    displayall()


# clearall
def cleartheall():
    id.set("")
    name.set("")
    age.set("")
    gender.set("")
    contact.set("")
    address.set("")
    solt.set("")


# search
def search():
    tv.selection()
    fetchdata = tv.get_children()
    for f in fetchdata:
        tv.delete(f)

    try:
        con = sqlite3.connect("compars")
        core = con.cursor()
        sql = " select * from compars where name = '%s' or gender = '%s' or solt = '%s' or address = '%s' or id = '%s' or contact = '%s' or age = '%s'"
        name = view_window_ent.get()
        core.execute(sql % (name, name, name, name, name, name, name))
        data = core.fetchall()
        if bool(data) == True:
            for d in data:
                tv.insert("", END, values=d)
        else:
            messagebox.showerror("Error in Input", "No Data Found")
            clearall()
            displayall()

    except Exception as e:
        showerror("issue", e)


# reset
def reset():
    tv.delete(*tv.get_children())
    for row in db.select():
        tv.insert("", END, values=row)
    clearall()


# clearall
def clearall():
    view_window_ent.delete(0, END)


# Back page
def loginnext():
    root.destroy()
    import main


# Main page
def menu():
    root.destroy()
    import compound


# logout
def logout():
    root.destroy()
    import create


# btn for delete, edit , pages
btn_frame = Frame(entry_frame, bg="#2c3e50")
btn_frame.grid(row=1, columnspan=6, padx=50, pady=10)

btn_add = Button(btn_frame, width=11, command=menu, text="MAIN MENU", font=("calibri", 10, "bold"), bg="white",
                 fg="dodgerblue4", bd=0)
btn_add.grid(row=0, column=0, padx=10, pady=10, sticky="w")

btn_delete = Button(btn_frame, width=11, command=delete_compars, text="DELETE ", font=("calibri", 10, "bold"),
                    bg="white", fg="dodgerblue4", bd=0)
btn_delete.grid(row=1, column=6, padx=10, pady=10, sticky="w")

btn_login = Button(btn_frame, width=11, command=loginnext, text="ADD COMPARS", font=("calibri", 10, "bold"), bg="white",
                   fg="dodgerblue4", bd=0)
btn_login.grid(row=0, column=1, padx=10, pady=10, sticky="w")

btn_edit = Button(btn_frame, width=11, command=update_compars, text="EDIT DETAILS", font=("calibri", 10, "bold"),
                  bg="white", fg="dodgerblue4", bd=0)
btn_edit.grid(row=2, column=6, padx=10, pady=10, sticky="w")

# btn for search
view_window_ent = Entry(btn_frame, width=10, font=('calibri', 12))
view_window_ent.grid(row=0, column=4, padx=10, pady=10, sticky="w")

btn_view = Button(btn_frame, command=search, width=10, text="SEARCH", font=("calibri", 10, "bold"), bg="white",
                  fg="dodgerblue4")
btn_view.grid(row=0, column=5, padx=10, pady=10, sticky="w")

btn_view = Button(btn_frame, command=reset, width=10, text="RESET", font=("calibri", 10, "bold"), bg="white",
                  fg="dodgerblue4", bd=0)
btn_view.grid(row=0, column=6, padx=10, pady=10, sticky="w")

# logout btn
btn_view = Button(btn_frame, command=logout, width=10, text="LOGOUT", font=("calibri", 10, "bold"), bg="white",
                  fg="dodgerblue4", bd=0)
btn_view.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Label for id to slot

txtname = Entry(btn_frame, width=10, textvariable=name, font=("calibri", 12), bg="white", fg="black")
txtname.grid(row=2, column=0, padx=10, pady=10, sticky="w")

txtage = Entry(btn_frame, textvariable=age, width=10, font=("calibri", 12), bg="white", fg="black")
txtage.grid(row=2, column=1, padx=10, pady=10, sticky="w")

combogender = ttk.Combobox(btn_frame, textvariable=gender, width=8, font=("calibri", 12), state="readonly")
combogender['values'] = ('Male', 'Female', 'Transgender')
combogender.grid(row=2, column=2, padx=10, pady=10, sticky="w")

txtcontact = Entry(btn_frame, textvariable=contact, width=10, font=("calibri", 12), bg="white", fg="black")
txtcontact.grid(row=2, column=3, padx=10, pady=10, sticky="w")

txtaddress = Entry(btn_frame, textvariable=address, width=10, font=("calibri", 12), bg="white", fg="black")
txtaddress.grid(row=2, column=4, padx=10, pady=10, sticky="w")

combosolt = ttk.Combobox(btn_frame, textvariable=solt, width=8, font=("calibri", 12), state="readonly")
combosolt['values'] = ('Solt-1 (LOIN)', 'Solt-2 (DEAR)', 'Solt-3 (WOLF)')
combosolt.grid(row=2, column=5, padx=10, pady=10, sticky="w")

# treeview (data show from db)
tree_frame = Frame(root, bg="orange")
tree_frame.place(x=0, y=280, width=900, height=300)

style = ttk.Style()
style.configure("mystyle.Treeview", font=("calibri", 8), rowheight=30)
style.configure("mystyle.Treeview.Heading", font=('calibri', 10))

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")

# scrollbar
vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tv.yview)
vsb.pack(side='right', fill='y')
tv.configure(yscrollcommand=vsb.set)

# tv heading
tv.heading("1", text="ID")
tv.column("1", width=2)
tv.heading("2", text="Name")
tv.column("2", width=5)
tv.heading("3", text="Age")
tv.column("3", width=2)
tv.heading("4", text="Gender")
tv.column("4", width=5)
tv.heading("5", text="Contact")
tv.column("5", width=5)
tv.heading("6", text="Address")
tv.column("6", width=5)
tv.heading("7", text="Solt")
tv.column("7", width=5)
tv['show'] = 'headings'
tv.bind('<ButtonRelease-1>', getData)
tv.pack(fill=X)

displayall()
root.mainloop()
