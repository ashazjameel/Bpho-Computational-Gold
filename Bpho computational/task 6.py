#task 6
import matplotlib.pyplot as plt
import numpy as np
import math

#parameters
r = 65/1000
d = 0.123 * 10**-9
V = 5 * 1000

x = 20              #blur effect, set to 1 for no blur
###

h = 6.626 * 10**-34
m = 9.109 * 10**-31
e = 1.60 * 10**-19
c = 2.998 * 10**8
mm = 1/1000

def calc(V):
    x = []
    p = (2*m*e*V)**0.5
    n_max = int((2**0.5)*d*p/h)
    for n in range(1,n_max+1):
        theta = 2*math.asin((n*h)/(2*d*p))
        x.append(r*math.sin(2*theta))
    return x

def plot(i):
    for t in range(x):
            circ = plt.Circle((0,0), i+0.1*t, fill=False, ec="#00FF00",alpha=1-(t/x)**0.1)
            circ2 = plt.Circle((0,0), i-0.1*t, fill=False, ec="#00FF00",alpha=1-(t/x)**0.1)
            ax.add_artist(circ)
            ax.add_artist(circ2)


ax = plt.gca()
ax.set_aspect("equal")
ax.set_facecolor("#019A00")
plt.xlim(-r/mm-1,r/mm+1)
plt.ylim(-r/mm-1,r/mm+1)
plt.suptitle(f"Electron diffraction: V = {V/1000} kV", y=0.95)
plt.xlabel("/mm")
plt.ylabel("/mm")
for i in calc(V):
    plot(i/mm)

plt.show()





#task 6a
V_array = np.linspace(1*1000,5*1000,100)
p = np.power(np.multiply(2*m*e,V_array),0.5)
V_array = np.power(V_array,-0.5)
n = 1
theta_array = (n*h)/(2*d)
theta_array = np.divide(theta_array,p)

delta_x = np.max(theta_array)-np.min(theta_array)
delta_y = np.max(V_array)-np.min(V_array)
gradient = delta_y/delta_x
d_calculated = n*h/(2*(2*m*e)**0.5)*gradient
print(d_calculated)

plt.scatter(theta_array,V_array*1000)
plt.suptitle("sin(0.5×Φ) vs 1/√V", y=0.95)
plt.xlabel("sin(0.5×Φ)")
plt.ylabel("1/√V (×10³)")
plt.show()















