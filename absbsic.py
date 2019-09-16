# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:18:27 2019

@author: Igor C
"""

import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop()