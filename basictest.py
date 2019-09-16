# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:59:12 2019

@author: Igor C
"""

import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack()

label1 = tk.Label(root, fg="dark green")
label1.config(text="test")
label1.pack()

label2 = tk.Label(root, fg="dark green")
label2.config(text="test")
label2.pack()


slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack()
root.mainloop()

print("k")