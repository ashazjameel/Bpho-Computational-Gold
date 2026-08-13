#task 1
import matplotlib.pyplot as plt
import numpy as np
try:
    import keyboard
except:
    print("ERROR: library 'keyboard' not installed, install it by typing 'pip3 install keyboard' into command prompt")
    raise ModuleNotFoundError("")


#parameters
N = 1000            #steps
s = 0.1                #step-size
points = 50
#######


##2d plot

theta = np.multiply(np.random.rand(points,N),2*np.pi)
dx = np.multiply(np.cos(theta),s)
dy = np.multiply(np.sin(theta),s)
X = np.cumsum(dx,1)
Y = np.cumsum(dy,1)

def plot1(X,Y,i,title,subtitle, **kwargs):
    font_size = kwargs.get("font_size", "xx-large")
    y = kwargs.get("y",0.96)
    plt.clf()
    ax = plt.gca()
    ax.set_aspect("equal")
    plt.suptitle(title,fontsize=font_size,y=y)
    plt.title(subtitle, fontsize="10",y=-0.15)
    for p in range(points):
        plt.plot(X[p][:i],Y[p][:i], lw=0.5)
    plt.pause(0.0001)

def plot2(X,Y,Z,i,title,subtitle):
    plt.clf()
    ax = plt.axes(projection="3d")
    ax.set_aspect("equal")
    plt.suptitle(title,fontsize="xx-large",y=0.96)
    plt.title(subtitle, fontsize="10",y=-0.15)
    for p in range(points):
        plt.plot(X[p][:i],Y[p][:i],Z[p][:i], lw=0.5)
    plt.pause(0.0001)
    
#animation
print(f"N = {N}, s = {s}, particle_count = {points}")
print("Playing 2D random walk animation...")

for i in range(N):
    if keyboard.is_pressed("enter"):
        break
    if keyboard.is_pressed("space"):
        plot1(X,Y,i,"2D Random walk animation","press P to unpause")
        plot1(X,Y,i,"2D Random walk animation","press P to unpause")
        keyboard.wait("p")
    plot1(X,Y,i,"2D Random walk animation", "press Enter to skip, press Space to pause")

#static plot
plot1(X,Y,len(X[0]), f"Random walk\nN = {N}, s = {s}, particle count = {points}", "Close the graph to continue", font_size="16",y=0.98)
plt.show()

print("Finished 2D plot, close the graph to play 3D animation")

##3d plot
print("Playing 3D random walk animation...")

u1,u2 = np.random.rand(points,N), np.random.rand(points,N)
dz = 2*u1-1
dx = ((1-dz**2)**0.5)*np.cos(2*np.pi*u2)
dy = ((1-dz**2)**0.5)*np.sin(2*np.pi*u2)

X,Y,Z = np.cumsum(dx,1), np.cumsum(dy,1), np.cumsum(dz,1)

fig = plt.figure()
ax = plt.axes(projection="3d")

for i in range(N):
    if keyboard.is_pressed("enter"):
        break
    if keyboard.is_pressed("space"):
        plot2(X,Y,Z,i,"3D Random walk animation", "press P to unpause")
        plot2(X,Y,Z,i,"3D Random walk animation", "press P to unpause")
        keyboard.wait("p")
    plot2(X,Y,Z,i,"3D Random walk animation", "press Enter to skip, press Space to pause")

plot2(X,Y,Z,len(X[0]),"3D Random walk",f"N = {N}, s = {s}, particle count = {points}")
plt.show()
print("Finished all plots")





#https://math.stackexchange.com/q/3184545
#https://en.wikipedia.org/wiki/Lambert_cylindrical_equal-area_projection
