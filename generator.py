import random
from tkinter import *
from tkinter.ttk import *
def low():
    entry.delete(0, END) 
    parol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    for i in range (10+1):
        password = password + random.choice(parol)
    return password
def generate():
    password2 = low()
    a=entry.insert(10, password2)
    return a
root = Tk()
root.title("Random Password Generator")
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
root.mainloop()
