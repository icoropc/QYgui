# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:37:55 2019

@author: Igor C
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


#data1 = np.genfromtxt('ref2.txt',delimiter='\t')
#data2 = np.genfromtxt('sig2.txt',delimiter='\t')


data1 = np.genfromtxt('blank.txt',skip_header=16,delimiter='\t')
data2 = np.genfromtxt('sample.txt',skip_header=16,delimiter='\t')

bckgdcounts=0

laser_signal_ref=0
fluor_signal_ref=0

laser_signal_sample=0
fluor_signal_sample=0


#ADD STUFF HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

lbound_low=395
lbound_high=410

fbound_low=580  
fbound_high=700

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

print(fluor_signal_sample)
print(QY)
#fig, ax = plt.subplots()
#
#plt.plot(data1[:,0],data1[:,1]-bckgdcounts,color='black')
#plt.plot(data2[:,0],data2[:,1]-bckgdcounts,color='red')
#
#ax.set_xlabel('Wavelength (nm)')
#ax.set_ylabel('PL (AU)', color='black')
#ax.set_xlim(370,750)
#ax.set_ylim(-1)        
#plt.text(500,200,"Laser sig ref: "+str(int(laser_signal_ref)))
#plt.text(500,150,"Laser sig sample: "+str(int(laser_signal_sample)))
#plt.text(500,100,"PL sig sample: "+str(int(fluor_signal_sample)))
#plt.text(500,50,"QY: "+str(round(QY,3)))
#
#axins2 = inset_axes(ax, width="100%", height="100%", loc='upper left',
#                   bbox_to_anchor=(0.65,0.55,0.3,0.4), bbox_transform=ax.transAxes)
#plt.plot(data1[:,0],data1[:,1],color='black')
#plt.plot(data2[:,0],data2[:,1],color='red')
#axins2.set_xlim(lbound_low,lbound_high)
#axins2.set_ylim(-30)
#
#axins3 = inset_axes(ax, width="100%", height="100%", loc='upper left',
#                   bbox_to_anchor=(0.20,0.55,0.3,0.4), bbox_transform=ax.transAxes)
#plt.plot(data1[:,0],data1[:,1],color='black')
#plt.plot(data2[:,0],data2[:,1],color='red')
#axins3.set_xlim(fbound_low,fbound_high)
#axins3.set_ylim(-0,0.02)