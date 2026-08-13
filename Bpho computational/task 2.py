#task 2
import matplotlib.pyplot as plt
import numpy as np



#parameters
N = 1000                 #small particles
T = 100                 #temp of air
m = 4.8*(10**-26)           #mass of air particle in kg
M = 10*m            #mass of large particle
r = 0.16              #radius of small particle
R = 10*r             #radius of large particle
a = 7*R              #modelling scene
C = 1                   #Coefficient of resitution
Kn = 100               #Knudsen's number

#average speeds in nm/ps
k_B = 1.38*(10**-23)        #Boltzmann's constant
v = (3*k_B*(T+273)/m)**0.5
V = (3*k_B*(T+273)/M)**0.5
v = v/1000
V = V/1000
dt = 0.01*Kn*r/v
touch_dist = (R+r)**2
big_positions_x = []
big_positions_y = []

def plot1(x,y,X,Y,positions_x,positions_y):
    plt.clf()
    plt.scatter(x,y,s=(r**2)*75)
    ax = plt.gca()
    ax.add_artist(plt.Circle((X,Y),R,fill=False))
    ax.set_aspect("equal")
    plt.suptitle("Brownian Motion Simulation", y = 0.95)
    plt.title(f"N = {N}, T = {T}℃, m₁ = {m}kg, m₂ = {M}kg, C = {C}, Kn = {Kn}", fontsize="10",y=-0.15)
    plt.xlim(0,a)
    plt.ylim(0,a)
    plt.plot(positions_x,positions_y,c="red",lw=0.5)
    plt.pause(0.0001)

def push(x,y,X,Y):
    if np.any(dist_squared(x,y,X,Y)):
        delta_pos = np.array([x-X,y-Y])
        norm_delta_pos = np.divide(delta_pos,np.linalg.norm(delta_pos))
        norm_delta_pos = np.multiply(norm_delta_pos,R)
        return np.add(np.array([x,y]),norm_delta_pos)
    return np.array([x,y])
        
    
def bounce(x_pos,y_pos,theta,X_pos,Y_pos,u2):
    u1 = np.array([np.cos(theta),np.sin(theta)])*v
    V = u1*m+u2*M
    V = np.divide(V,m+M)
    v1 = C*(V-u1)+V
    v2 = C*(V-u2)+V
    x_pos,y_pos = x_pos + v1[0]*dt, y_pos + v1[1]*dt
    x_pos,y_pos = push(x_pos,y_pos,X_pos,Y_pos)
    return x_pos, y_pos, v2

def dist_squared(x,y,X,Y):
    dist_sqrd_x = (np.subtract(x,X))**2
    dist_sqrd_y = (np.subtract(y,Y)**2)
    dist_sqrd = dist_sqrd_x+dist_sqrd_y 
    out = np.less_equal(dist_sqrd,touch_dist)
    return out

small_X = np.random.rand(N)*a
small_Y = np.random.rand(N)*a
big_X = a/2
big_Y = a/2
check = dist_squared(small_X,small_Y,big_X,big_Y)
while np.any(check):        #preventing them from spawning inside the large particle
    for i in range(N):
        if check[i]:
            small_X[i] = np.random.rand()*a
            small_Y[i] = np.random.rand()*a
    check = dist_squared(small_X,small_Y,big_X,big_Y)
    
big_velocity = np.random.rand()*2*np.pi
big_velocity = np.array([np.cos(big_velocity),np.sin(big_velocity)])*V

plot1(small_X,small_Y,big_X,big_Y,big_positions_x,big_positions_y)

while True:
    theta = np.random.rand(N)*2*np.pi
    dx = np.cos(theta)*v*dt
    dy = np.sin(theta)*v*dt
    small_X = small_X+dx
    small_Y = small_Y+dy
    big_X = big_X + big_velocity[0]*dt
    big_Y = big_Y + big_velocity[1]*dt
    touches = dist_squared(small_X,small_Y,big_X,big_Y)
    if np.any(touches) == False:
        continue
    else:
        for i in range(N):
            if touches[i]:
                small_X[i], small_Y[i], big_velocity = bounce(small_X[i],small_Y[i],theta[i],big_X,big_Y,big_velocity)
    big_positions_x.append(big_X)
    big_positions_y.append(big_Y)
    #print(big_positions)
    plot1(small_X,small_Y,big_X,big_Y,big_positions_x,big_positions_y)





    
