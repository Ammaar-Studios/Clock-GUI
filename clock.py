from operator import length_hint
from sre_parse import DIGITS
from tkinter import *
from tkinter.ttk import *

from time import strftime
from turtle import width

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("IMPACT", 80), background = "black", foreground = "yellow")
label.pack(anchor='center')
time()

mainloop()