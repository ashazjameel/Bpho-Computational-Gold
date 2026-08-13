#task 4
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk

#parameters
n = 1000                #points to plot
W_dict = {"Silver":(4.3,"#989898"),"Aluminium":(4.3,"#D6D6D6"),"Gold":(5.1,"#FAD457"),"Copper":(4.7,"#DA7C58"),"Tin":(4.4,"#868887"),"Lead":(4.3,"#8E8FA4"),"Tungsten":(4.5,"#A69784"),"Nickel":(4.6,"#434135"),"Sodium":(2.4,"#B3B4AC")}
f_max = 2.5 * 10**15
###


h = 6.626 * 10**-34
e = 1.602176620898 * 10**-19

def voltage(f,W):
    return np.subtract(np.multiply(f,h/e),W)

def plot_colours():
    plt.axvline(4.62 * 10**14, c="#FF0000", lw=1)
    plt.axvline(5.16 * 10**14, c="#FFFF00", lw=1)
    plt.axvline(5.45 * 10**14, c="#00FF00", lw=1)
    plt.axvline(5.99 * 10**14, c="#00FFFF", lw=1)
    plt.axvline(6.66 * 10**14, c="#0000FF", lw=1)

def plot1(W,name):
    f_cutoff = W*e/h
    f0_n = int((f_cutoff/f_max)*n)
    f1_n = n-f0_n
    f0, f1 = np.linspace(0,f_cutoff, f0_n), np.linspace(f_cutoff,f_max,f1_n)

    plt.clf()
    plt.title(f"Photoelectric effect of {name}: W = {W}eV")
    plt.xlabel("Frequency /Hz")
    plt.ylabel("Stopping voltage /volts")
    plt.plot(f0, voltage(f0,W), c="#FF00FF", ls="--")
    plt.plot(f1, voltage(f1,W), c="#FF00FF")
    plt.axvline(f_cutoff, c="#FF00FF", ls="--", lw=1)
    plot_colours()
    plt.show()

def update(eventObject):
    metal = cb.get()
    print(f"Selected: {metal}")
    metal_plate = frame.create_rectangle(115,97,120,250, width=0, fill=W_dict[metal][1])
    plot1(W_dict[metal][0],metal)

root = Tk()
root.title("Photoelectric effect simulation")
root.config(bg="#B8F3FF")
root.geometry("800x450")

frame = Canvas(root, width = 600, height=400)
frame.pack(anchor=NW)

lamp = PhotoImage(file="lamp.png")
frame.create_image(200, 55, image=lamp)

stand = PhotoImage(file="stand.png")
frame.create_image(250, 230, image=stand)

cb = ttk.Combobox(root, values=list(W_dict.keys()), state="readonly")
cb.set("Select a metal")
cb.pack()

cb.bind("<<ComboboxSelected>>", update)
root.mainloop()












