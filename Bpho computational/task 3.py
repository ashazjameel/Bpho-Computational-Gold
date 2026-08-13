#task 3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

#parameter
n = 25000                            #total points to plot
final_lambda = 2500             #final lambda plotted
T_array = np.arange(4000,9000,1000)                               #temperature in kelvin
#######


nm = 10**-9
k_B = 1.381*(10**-23)
h = 6.626*(10**-34)
c = 2.998*(10**8)
T_labels = []

def B(Lambda, T):
    return np.divide(2*h*c**2,np.multiply((np.power(Lambda,5)),np.power(np.e,np.divide(h*c,np.multiply(Lambda,T*k_B)))-1))

def settings(setting):
    plt.xlabel("Wavelength /nm", fontsize=12)
    if setting==2:
        plt.suptitle("Solar Irradiance vs Wavelength",y=0.95)
        plt.ylabel("Irradiance /Wm⁻²/nm (×10¹⁴)", fontsize=12)
    else:
        if setting == 3:
            plt.suptitle("Solar Irradiance and Temperature vs Wavelength",y=0.95)
        elif setting == 4:
            plt.suptitle("Contour map of Solar Irradiance and Temperature vs Wavelength",y=0.95)
        plt.ylabel("Temperature /K", fontsize=12)
        ax.set_zlabel("Irradiance /Wm⁻²/nm (×10¹⁴)", fontsize=12)
        
Lambda_array = np.linspace(0,final_lambda*nm,num=n)

#first plot
for T in T_array:
    B_array = B(Lambda_array,T)
    plt.plot(np.divide(Lambda_array,nm),np.divide(B_array,10**14))
    T_labels.append(str(T)+"K")

settings(2)
plt.legend(T_labels)
plt.show()

#second plot
T_array = np.arange(4000,9000,100)
X,Y = np.meshgrid(Lambda_array,T_array)
Z = B(X,Y)

fig = plt.figure()
ax = plt.axes(projection="3d")

plt.plot(np.divide(X,nm), Y, np.divide(Z,10**14), color="blue")
settings(3)
plt.show()

#third plot
fig = plt.figure()
ax = plt.axes(projection="3d")

ax.contour3D(np.divide(X,nm), Y, np.divide(Z,10**14), 100)
settings(4)
plt.show()


#part 2
step_size = 1
T_array = np.arange(1,800+step_size,step_size)                               #temperature in kelvin

R = 8.314

def C(T_D,T):
    T_E = T_D*((np.pi/6)**(1/3))
    f_E = k_B*T_E/h
    x = np.divide((h*f_E)/k_B,T)
    return np.divide(np.multiply(np.multiply(3*R,np.power(x,2)),np.exp(x)), np.power(np.exp(x)-1,2))

f = open("task 3 data.txt","r",encoding="utf-8")
text = f.read().splitlines()

elements = dict()               #elements and their corresponding Debye temperatures at 0K and 298K
for i in text:
    b = i[1:-1]
    b = b.replace("'","")
    b = b.replace('"',"")
    b=b.split(", ")
    if len(b)==3:
        elements[b[0]] = (b[1],"N/A",b[2])
    elif "none" in b:
        elements[b[0]] = ("N/A",b[2],b[3])
    else:
        elements[b[0]] = (b[1],b[2],b[3])

print("plotting Einstein's model of heat capacity")
for element in elements:
    T_D = elements[element][0]              #0k and 298k
    colour = elements[element][-1]
    if T_D == "N/A":
        continue
    T_D = float(T_D[:-1])
    #plt.clf()
    plt.plot(T_array,C(T_D,T_array),c=colour)
    plt.legend([element], loc="lower right")
    plt.pause(0.1)

plt.show()















#Source: "https://www.knowledgedoor.com/2/elements_handbook/debye_temperature.html",
#Date of access: 9Aug/2026 17:52 (BST)
#Colours taken from Google Images or from online colour palettes (may not be 100% scientifically accurate)
