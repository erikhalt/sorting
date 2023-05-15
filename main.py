from tkinter import *
import sys
from numpy_data import generate_data
import matplotlib.pyplot as plt
import numpy as np
import random
import time

from bubble_sort import bubble_sort

#Config
full_window_size = '800x800'
canvas_width = 800
canvas_height = 600
window = Tk()
window.geometry(full_window_size)
title = Label(window,text='Sorting Algorithm')
title.pack()


def draw_rectangle(data):
    x_offset = 5
    bar_widht = 20
    global canvas
    canvas.delete('all')
    for idx,i in enumerate(data):
        x_pos = idx*(bar_widht+x_offset)+25
        canvas.create_rectangle(x_pos,600,x_pos+bar_widht,600-i,fill='red',)
    window.update_idletasks()


canvas = Canvas(window,bg='lightblue',width=canvas_width,height=canvas_height)
canvas.place(y=200)
UI = Canvas(window,bg='grey',width=800,height=200)
UI.place(y=0)
datalist = []

def generate():
    global datalist
    datalist = generate_data(30)
    draw_rectangle(datalist)
    return  datalist


def startbubble():
    global datalist
    for i in range(len(datalist)):
        bubble_sort(datalist,draw_rectangle)
    

Button(UI, text="BubbleSort", command=startbubble, bg='red').place(y=50,x=150)
Button(UI, text="GenerateData", command=generate, bg='red').place(y=50,x=50)


window.mainloop()
