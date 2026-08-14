#task 4
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from time import sleep as wait

#parameters
n = 1000                #points to plot
W_dict = {"Silver":(4.3,"#989898"),"Aluminium":(4.3,"#D6D6D6"),"Gold":(5.1,"#FAD457"),"Copper":(4.7,"#DA7C58"),"Tin":(4.4,"#868887"),"Lead":(4.3,"#8E8FA4"),"Tungsten":(4.5,"#A69784"),"Nickel":(4.6,"#434135"),"Sodium":(2.4,"#B3B4AC")}
f_max = 2.5 * 10**15
###


h = 6.626 * 10**-34
e = 1.602176620898 * 10**-19
c = 2.998*10**8

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

frame = Canvas(root, width = 600, height=375)
frame.pack(anchor=NW)

lamp = PhotoImage(file="lamp.png")
frame.create_image(200, 55, image=lamp)

stand = PhotoImage(file="stand.png")
frame.create_image(250, 230, image=stand)

cb = ttk.Combobox(root, values=list(W_dict.keys()), state="readonly")
cb.set("Select a metal")
cb.pack()

cb.bind("<<ComboboxSelected>>", update)

is_touched = False

def to_rgb(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"

def light_draw(R,G,B):
        frame.create_polygon([[220,100],[120,250],[120,150],[165,70]],fill="",width=5,outline=to_rgb(R,G,B))

def elect():
    global is_touched
    if not is_touched:
        is_touched = True
        if cb.get()!="Select a metal":
            f_0 = W_dict[cb.get()][0]*e/h
            if c/(var1.get()*10**-9) > f_0:
                print("electron emitted")
                electron_list.append(0)
                pos_list.append(0)
                frame.create_oval(120,175,140,155,tags=f"electron")
                move()
        root.after(1000,untouch)
        root.after(1000,elect)

electron_list = []
pos_list = []
dx1=100
"""
def move(pos):
    print("a")
    if pos_list[pos]>500:
        pass
        #root.after_cancel(root)
    else:
        pos_list[pos] = pos_list[pos] + dx1
        frame.move(f"electron{pos}",dx1,0)
        root.after(1,move(pos))"""

def move():
    frame.move("electron",dx1,0)
    root.after(10,move)

"""
electron_list.append(0)
pos_list.append(0)
frame.create_oval(120,175,140,155,tags=f"electron{len(electron_list)-1}")
move(len(electron_list)-1)"""

def untouch():
    global is_touched
    is_touched=False

#http://www.noah.org/wiki/Wavelength_to_RGB_in_Python
#http://www.physics.sfasu.edu/astro/color/spectra.html
def light_func(eventObject):
    elect()
    wavelength = var1.get()
    if wavelength<380 or wavelength>750 :
        light_draw(0,0,0)
    else:
        if wavelength>=380 and wavelength<=440:
            attenuation = 0.3 + 0.7*(wavelength-380) / (440-380)
            R = ((-(wavelength-440) / (440-380)) * attenuation) ** 0.8
            G = 0
            B = attenuation**0.8
        elif wavelength >= 440 and wavelength <= 490:
            R = 0
            G = ((wavelength-440)/(490-440))**0.8
            B = 1
        elif wavelength >= 490 and wavelength <= 510:
            R=0
            G=1
            B=(-(wavelength-510) / (510-490)) ** 0.8
        elif wavelength >= 510 and wavelength <= 580:
            R=((wavelength-510)/(580-510))**0.8
            G=1
            B=0
        elif wavelength >=580 and wavelength<=645:
            R=1
            G=(-(wavelength-645)/(645-580))**0.8
            B=0
        elif wavelength>=645 and wavelength<=750:
            attenuation = 0.3+0.7*(750-wavelength)/(750-645)
            R = attenuation**0.8
            G=0
            B=0
        R,G,B = min(255,int(R*256)),min(255,int(G*256)),min(255,int(B*256))
        light_draw(R,G,B)
        
            

var1=IntVar()
S1 = Scale(root, orient=HORIZONTAL, from_=100, to=850, variable=var1, command=light_func)
S1.place(relx=0.15, rely=0.95, anchor=CENTER, width=150)
l1=Label(root, text="Wavelength /nm")
l1.place(relx=0.09,rely=0.85)

root.mainloop()








