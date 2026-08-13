#task 8
from tkinter import *
import math

def draw_arrows(eventObject):
    frame.delete("all")
    theta1, theta2 = float(var1.get())/180*math.pi, float(var2.get())/180*math.pi
    dx1, dy1 = math.sin(theta1)*125, math.cos(theta1)*125
    dx2, dy2 = math.sin(theta2)*125, math.cos(theta2)*125
    
    frame.create_line(200,150,200 + dx1,150 - dy1, arrow=LAST,fill="red",width=3)
    frame.create_line(200,150,200 + dy1,150 + dx1, arrow=LAST,fill="red",width=3)
    frame.create_line(200,150,200,0,dash="-")
    frame.create_arc(200-20,150-20,200+20,150+20,start = 90-theta1*180/math.pi, extent=theta1*180/math.pi)
    
    frame.create_line(600,150,600 + dx2,150 - dy2, arrow=LAST,fill="blue",width=3)
    frame.create_line(600,150,600 + dy2,150 + dx2, arrow=LAST,fill="blue",width=3)
    frame.create_line(600,150,600,0,dash="-")
    frame.create_arc(600-20,150-20,600+20,150+20,start = 90-theta2*180/math.pi, extent=theta2*180/math.pi)

    frame.create_line(400,150,400 + dx1,150 - dy1, arrow=LAST,fill="red",width=3)
    frame.create_line(400,150,400 + dy1,150 + dx1, arrow=LAST,fill="red",width=3)
    frame.create_line(400,150,400 + dx2,150 - dy2, arrow=LAST,fill="blue",width=3)
    frame.create_line(400,150,400 + dy2,150 + dx2, arrow=LAST,fill="blue",width=3)
    
    t = theta1-theta2
    frame.create_arc(400-20,150-20,400+20,150+20,start = 90-(min(theta1,theta2))*180/math.pi, extent=(-abs(t))*180/math.pi)
    classical()
    quantum()

def classical():
    theta1, theta2 = float(var1.get())/180*math.pi, float(var2.get())/180*math.pi
    mismatch = 1 - (math.cos(theta1)*math.cos(theta2))**2 -(math.sin(theta1)*math.sin(theta2))**2
    l_classical.config(text=f"Classical: {mismatch}")

def quantum():
    theta1, theta2 = float(var1.get())/180*math.pi, float(var2.get())/180*math.pi
    mismatch = math.sin(theta1-theta2)**2
    l_quantum.config(text=f"Quantum: {mismatch}")

root = Tk()
root.title("Visual calculator")
root.config(bg="#B8F3FF")
root.geometry("800x450")

frame = Canvas(root, width = 800, height=300)
frame.pack(anchor=NW)


var1,var2 = DoubleVar(), DoubleVar()
l1=Label(root, text="Theta (°)")
l2=Label(root, text="Phi (°)")

S1 = Scale(root, orient=HORIZONTAL, from_=-180, to=180, variable=var1, command=draw_arrows)
S1.place(relx=0.25, rely=5/6, anchor=CENTER, width=150)
S2 = Scale(root, orient=HORIZONTAL, from_=-180, to=180, variable=var2, command=draw_arrows)
S2.place(relx=0.75, rely=5/6, anchor=CENTER, width=150)
l1.place(relx=0.22,rely=5/6-0.1), l2.place(relx=0.7275,rely=5/6-0.1)
S1.set(180), S2.set(180)
S1.set(0), S2.set(0)

l_classical=Label(root, text="Classical: ")
l_quantum=Label(root, text="Quantum: ")
l_classical.place(relx=0.4,rely=4/6+0.1),l_quantum.place(relx=0.4,rely=4/6+0.15)


root.mainloop()
