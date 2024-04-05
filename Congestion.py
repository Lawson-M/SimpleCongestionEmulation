import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random
import array


def Congest(size, delay):

    sizeLeft = size
    AckCount = 0
    win = 1
    time = 0
    triAck = 0
    pktT = 0
    pktA = 0

    arrx = []
    arry = []

    def plotIt(x,y):
        fig, ax = plt.subplots()  # Create a figure containing a single axes.
        ax.plot(x, y)  # Plot some data on the axes
        plt.show()
    

    random.seed(version=2)
    while(sizeLeft>0):
        
        if (win<8): #Slow Start
            win = win*2
        else:
            win = win+1
        
        #Rolls random number for Timeout and Tripple ACK
        ranTime = random.randrange(1,100,1)

        #Timeout
        if ranTime>=95:
            win = 1
            pktT = pktT+1

        #Triple ACK
        if 95>ranTime>90:
            triAck = triAck + 1
            if triAck>2:
                win = win/2
                triAck=0
                pktA = pktA+1
        
        #Store Current interval and ms
        arry.insert(time, win)
        arrx.insert(time, time)
        
        time = time+1
        sizeLeft = sizeLeft-win

    plotIt(arrx,arry)
    tput = size/time
    L1=tk.Label(master, text=tput)
    L2=tk.Label(master, text=pktT)
    L3=tk.Label(master, text=pktA)
    L4=tk.Label(master, text=time)
    L1.grid(row=2, column=1)
    L2.grid(row=3, column=1)
    L3.grid(row=4, column=1)
    L4.grid(row=5, column=1)

        
        
    


master = tk.Tk()
master.geometry('600x300')
master.configure(bg="#E6DBD0")
master.tk.call('tk', 'scaling', 1)

e1 = tk.Entry(master)
e1.grid(row=0, column=1)



tog = tk.Button(master, text="Enter", command=lambda: Congest(int(e1.get()),0), bg="#439775", activebackground="grey")
tog.grid(row=1, column=1)

tk.Label(master, text='Bytes:').grid(row=0, column=0)
tk.Label(master, text='Total Throughput (bpms):').grid(row=2, column=0)
tk.Label(master, text='Packets Dropped (Timeout):').grid(row=3, column=0)
tk.Label(master, text='Packets Dropped (TriACK) :').grid(row=4, column=0)
tk.Label(master, text='Total time (ms) :').grid(row=5, column=0)

master.mainloop()

