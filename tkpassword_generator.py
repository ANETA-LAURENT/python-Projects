####password generator####

import random as r
import string as s
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Password Generator")
root.geometry("600x500+50+50")
root.attributes("-topmost", 1)
root.configure(bg="white")

canvas1 = tk.Canvas(root, width=400, height=400, relief="raised")
canvas1.pack(expand=1)


label1 = tk.Label(root, text="Find your perfect strong password")
label1.config(font=("helvetica", 16))
label1.configure(bg="white")
canvas1.create_window(200, 35, window=label1)
canvas1.configure(bg="white")

label2 = tk.Label(
    root, text="Enter the length of password, \n min 8 and max 32 characters: "
)
label2.config(font=("helvetica", 13))
label2.configure(bg="white")
canvas1.create_window(200, 100, window=label2)


entry1 = tk.Entry(root, bd=4, width=2)
entry1.config(font=("helvetica", 16))
canvas1.create_window(200, 160, window=entry1)


def run():
    x1 = entry1.get()
    all = s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation

    password = r.choices(all, k=int(x1))
    final = "".join(password)

    label3 = tk.Label(
        root, text="Your password is: \n " + final, font=("helvetica", 13)
    )
    canvas1.create_window(200, 270, window=label3)
    label3.configure(bg="white")


def exit():
    MsgBox = tk.messagebox.askquestion(
        "Exit Application",
        "Are you sure you want to exit the application",
        icon="warning",
    )
    if MsgBox == "yes":
        root.destroy()
    else:
        tk.messagebox.showinfo(
            "Return", "You will now return to the application screen"
        )


button1 = tk.Button(
    text="Find",
    command=run,
    bg="brown",
    fg="white",
    activebackground="tomato",
    font=("helvetica", 12, "bold"),
)
canvas1.create_window(160, 220, window=button1)

button2 = tk.Button(
    text="Exit",
    command=exit,
    bg="black",
    fg="white",
    font=("helvetica", 12, "bold"),
)
canvas1.create_window(250, 220, window=button2)


root.mainloop()