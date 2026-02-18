from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
import tkinter as tk
#import sys
#import time

root = tk.Tk()
root.title('Tkinter calculator')
root.geometry('550x550')

root.columnconfigure(2, weight=1)
root.columnconfigure(0, weight=2)
root.columnconfigure(0, weight=3)
root.columnconfigure(0, weight=4)
root.columnconfigure(0, weight=5)
root.columnconfigure(0, weight=6)

frame = tk.Frame(root, borderwidth=50, relief="ridge", border=5)
frame.grid()

def calculate():
    try:
        result = eval(value.get())
        value.set(result)

    except:
        value.set("")
    
      
value = tk.StringVar(value ="")        
entry = tk.Entry(root, textvariable=value, font=("Arial", 14), justify='right', cursor="hand2", border=8)
entry.grid(ipadx=150, padx=100)

def clear():
    value.set("")

def change_colors():
    colors = askcolor(title= "Color chooser")
    root.configure(bg=colors[1])


def press(key: str):
    value.set(value.get() + key)

ttk.Button(root, text="0", command=lambda: press("0")).grid(column="2", row=8, pady=3, ipadx='8', ipady='10')
ttk.Button(root, text="1", command=lambda: press("1")).grid(column="1", row=3, pady=3, ipadx='8', ipady='10')
ttk.Button(root, text="2", command=lambda: press("2")).grid(column="2", row=3, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="3", command=lambda: press("3")).grid(column="3", row=3, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="4", command=lambda: press("4")).grid(column="1", row=4, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="5", command=lambda: press("5")).grid(column="2", row=4, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="6", command=lambda: press("6")).grid(column="3", row=4, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="7", command=lambda: press("7")).grid(column="1", row=5, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="8", command=lambda: press("8")).grid(column="2", row=5, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="9", command=lambda: press("9")).grid(column="3", row=5, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="+", command=lambda: press("+")).grid(column="1", row=6, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="-", command=lambda: press("-")).grid(column="2", row=6, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="/", command=lambda: press("/")).grid(column="3", row=6, pady=3, ipadx='8', ipady='8')
ttk.Button(root, text="*", command=lambda: press("*")).grid(column="1", row=7, pady=3, ipadx='8', ipady='8')


ttk.Button(
    root,
    text="Personnaliser!", #"Select a color boi",
    cursor="hand2",
    command=change_colors).grid(column='2', row='9', ipadx='10', ipady='10')

ttk.Button(
    root,
    text="C",
    cursor="hand2",
    command=clear).grid(column='3', row='7', ipadx='8', ipady='8')

ttk.Button(
    root,
    text="=",
    cursor="hand2",
    command=calculate).grid(column='2', row='7', ipadx='8', ipady='8')

#photo = PhotoImage(file="chat.png")
#imgLabel = Label(root, image=photo)
#imgLabel.grid(ipadx='8', ipady='8')

root.mainloop()
