# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:58:46 2019

@author: Igor Coropceanu
"""

import matplotlib as plt
import matplotlib
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
from backend import *
from tkinter import filedialog




LARGE_FONT= ("Verdana", 12)


class IntaDig(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

#        tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Sea of BTC client")
        
#        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select blank file",filetypes = (("text files","*.txt"),("all files","*.*")))
#        blankfile=self.filename
#        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select blank file",filetypes = (("text files","*.txt"),("all files","*.*")))
#        sampfile=root.filename
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, StartPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        

        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Load Reference File",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.LEFT)
        
        button2 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

#        f = Figure(figsize=(5,5), dpi=100)
#        a = f.add_subplot(111)
#        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])


        
        fig= Figure(figsize=(5,5))
        a = fig.add_subplot(111)
        a.plot(data1[:,0],data1[:,1]-bckgdcounts,color='black')
        a.plot(data2[:,0],data2[:,1]-bckgdcounts,color='red')

        ax=a.axes
        
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
        
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        axins3 = inset_axes(ax, width="100%", height="100%", loc='upper left',
                   bbox_to_anchor=(0.20,0.55,0.3,0.4), bbox_transform=ax.transAxes)
        axins3.plot(data1[:,0],data1[:,1],color='black')
        axins3.plot(data2[:,0],data2[:,1],color='red')
        axins3.set_xlim(fbound_low,fbound_high)
        axins3.set_ylim(-0,1)



        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



#root=tk.TK()
app =IntaDig()
app.mainloop()