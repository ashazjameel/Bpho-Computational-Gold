#task 7
import matplotlib.pyplot as plt
import numpy as np
try:
    import keyboard
except:
    print("ERROR: library 'keyboard' not installed, install it by typing 'pip3 install keyboard' into command prompt")
    raise ModuleNotFoundError("")

#parameters
m = 9.1094 * 10**-31
a = 5.25 * 10**-11
dt = 1 * 10**-37
###

h = 6.626 * 10**-34
h_bar = h/(2*np.pi)
e = 1.6 * 10**-19

def E_n(n):
    return np.divide(np.multiply((h_bar**2 * np.pi**2)/(2*m*a**2), np.power(n,2)), e)

n = np.linspace(0,3,100)
plt.plot(n,E_n(n), ls="--")
plt.scatter(range(1,4), E_n(range(1,4)), marker="x")
plt.title(f"Particle in a box energy /eV, m = {round(m,33)} kg")
plt.xlabel("Quantum number")
plt.ylabel("Energy /eV")
plt.grid()
plt.show()

def Psi(n,x,t):
    if t == 0:
        return np.power(np.multiply((2/a)**0.5, np.sin(np.multiply(n*np.pi/a,x))),2)
    else:
        return np.multiply(Psi(n,x,0), np.cos(t/h * E_n(n)))           #real part of wave equation

def plot1(t):
    plt.clf()
    plt.ylim(-4*10**10,4*10**10)
    plt.plot(x,Psi(1,x,t))
    plt.plot(x,Psi(2,x,t))
    plt.plot(x,Psi(3,x,t))
    plt.xlabel("x /angstroms")
    plt.ylabel("Probability density")
    plt.legend(labels, bbox_to_anchor=(1.122,1.1625), loc="upper right")

labels = []
for i in range(1,4):
    labels.append(f"n = {i}, E  = {round(E_n(i),4)} eV")

x = np.linspace(0,a,1000)
t = 0
plt.figure(figsize=(8.5,6.5))
plot1(0)
plt.ylim(0,4*10**10)
plt.suptitle(f"Particle in a box, m = {round(m,33)} kg",y=0.95)
plt.show()

fig = plt.figure(figsize=(8.5,6.5))
while True:
    if keyboard.is_pressed("enter"):
        plt.close(fig)
        break
    if keyboard.is_pressed("space"):
        plt.title("Press P to unpause", fontsize="10",y=-0.15)
        plt.pause(0.05)
        keyboard.wait("P")
        
    t += dt
    plot1(t)
    plt.suptitle(f"Animated particle in a box, t = {round(t* 10 **36,1)}×10⁻³⁶ s",y=0.95)
    plt.title("Press Enter to exit, Press Space to pause", fontsize="10",y=-0.15)
    plt.pause(0.05)
plt.show()









