# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:18:27 2019

@author: Igor C
"""

import tkinter as tk


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


#from backend import *

import numpy as np



root = tk.Tk()
root.wm_title("QY Calculation")




frame = tk.Frame(root)
l1 = tk.Label(frame, text = "xxxxxxxxxxxxxxxxxxxxxxxxx            ")
l2 = tk.Label(frame, text = "xxxxxxxxxxxxxxxxxxxxxxxxx            ")


l1.grid(row=0,column=1)
l2.grid(row=1,column=1)


ref_file=""
sample_file=""

root.ref_file="Null"
root.samp_file="Null"

def get_reffile():
    root.ref_file =tk.filedialog.askopenfilename(initialdir = "/",title = "Select reference file",filetypes = (("text files","*.txt"),("all files","*.*")))
    l1.config(text=str(root.ref_file))
def get_samplefile():
    root.samp_file =tk.filedialog.askopenfilename(initialdir = "/",title = "Select sample file",filetypes = (("text files","*.txt"),("all files","*.*")))
    l2.config(text=str(root.samp_file))

button1 = tk.Button(frame, text="Reference",command=get_reffile).grid(row=0,column=0)
button2 =tk.Button(frame, text="Sample",command=get_samplefile).grid(row=1,column=0)


frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

frame2 = tk.Frame(root)
l3 = tk.Label(frame2, text = "Laser low").grid(row=1,column=0)
v1 = tk.StringVar()
e3 = tk.Entry(frame2)
e3.grid(row=1,column=2)
e3.insert(0,"395")
l4 = tk.Label(frame2, text = "Laser high").grid(row=1,column=4)
e4 = tk.Entry(frame2)
e4.grid(row=1,column=5)
e4.insert(0,"410")
l5 = tk.Label(frame2, text = "pl low").grid(row=2,column=0)
e5 = tk.Entry(frame2)
e5.grid(row=2,column=2)
e5.insert(0,"580")
l6 = tk.Label(frame2, text = "pl high").grid(row=2,column=4)
e6 = tk.Entry(frame2)
e6.grid(row=2,column=5)
e6.insert(0,"700")
frame2.pack(side=tk.TOP,fill=tk.BOTH, expand=1)



fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




def add_plot():
    fig.clf()
    canvas.draw()
    
    a = fig.add_subplot(111)
    ax=a.axes

    data1 = np.genfromtxt(root.ref_file,skip_header=16,delimiter='\t')
    data2 = np.genfromtxt(root.samp_file,skip_header=16,delimiter='\t')

    
    bckgdcounts=0

    laser_signal_ref=0
    fluor_signal_ref=0
    
    laser_signal_sample=0
    fluor_signal_sample=0
    
        
    lbound_low=395
    lbound_high=410
    fbound_low=580  
    fbound_high=700

    lbound_low=int(e3.get())
    lbound_high=int(e4.get())
    fbound_low=int(e5.get())
    fbound_high=int(e6.get())
    
    for i in data1:
        if lbound_low<i[0]<lbound_high:
            laser_signal_ref+=i[1]*i[0]/1000
        elif fbound_low<i[0]<fbound_high:
            fluor_signal_ref+=i[1]*i[0]/1000
            
    for i in data2:
        if lbound_low<i[0]<lbound_high:
            laser_signal_sample+=i[1]*i[0]/1000
        elif fbound_low<i[0]<fbound_high:
            fluor_signal_sample+=i[1]*i[0]/1000
    
    QY=fluor_signal_sample/(laser_signal_ref-laser_signal_sample)

    a.plot(data1[:,0],data1[:,1]-bckgdcounts,color='black')
    a.plot(data2[:,0],data2[:,1]-bckgdcounts,color='red')
    
    a.text(500,200,"Laser sig ref: "+str(int(laser_signal_ref)))
    a.text(500,150,"Laser sig sample: "+str(int(laser_signal_sample)))
    a.text(500,100,"PL sig sample: "+str(int(fluor_signal_sample)))
    a.text(500,50,"QY: "+str(round(QY,3)))
    
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('PL (AU)', color='black')
    ax.set_xlim(370,750)
    ax.set_ylim(-1)        
    
    axins2 = inset_axes(ax, width="100%", height="100%", loc='upper left',
               bbox_to_anchor=(0.65,0.55,0.3,0.4), bbox_transform=ax.transAxes)
    axins2.plot(data1[:,0],data1[:,1],color='black')
    axins2.plot(data2[:,0],data2[:,1],color='red')
    axins2.set_xlim(lbound_low,lbound_high)
    axins2.set_ylim(-30)
    
    
    axins3 = inset_axes(ax, width="100%", height="100%", loc='upper left',
               bbox_to_anchor=(0.20,0.55,0.3,0.4), bbox_transform=ax.transAxes)
    axins3.plot(data1[:,0],data1[:,1],color='black')
    axins3.plot(data2[:,0],data2[:,1],color='red')
    axins3.set_xlim(fbound_low,fbound_high)
    axins3.set_ylim(-0,1)
    
    canvas.draw()    

def clear_canvas():
    fig.clf()
    canvas.draw()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


addplotbut = tk.Button(master=root, text="Calculate QY", command=add_plot)
addplotbut.pack()

clearplot = tk.Button(master=root, text="Clear plot", command=clear_canvas)
clearplot.pack()

button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.BOTTOM)



tk.mainloop()