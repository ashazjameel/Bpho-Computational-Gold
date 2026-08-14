#task 10
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import lpmv as P

#parameters
Z = 6               #proton number
N = 4               #principal quantum number
A = 12              #mass number
L = 2                #angular momentum quantum number
#######

E_0 = 8.854187817 * 10**-12
h = 6.62607004081 * 10**-34
m_e = 9.1093835611 * 10**-31
e = 1.602176620898 * 10**-19
a_0 = (E_0 * h**2)/(m_e * e**2 * np.pi) * 10**10        #in Angstroms
u = 1.6605402 * 10**-27

M = A*u
mu = (m_e*M)/(m_e+M)
a = (m_e*a_0)/(mu*Z)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def gamma(x_array,l,n):
    out_array = np.zeros(len(x_array))
    for k in range(n-l):
        cur = np.multiply(factorial(l+n),np.power(np.multiply(-1,x_array),k))
        cur = np.divide(cur,factorial(2*l+1+k)*factorial(n-l-1-k)*factorial(k))
        out_array = np.add(out_array, cur)
    return out_array

def R(r_array,n,l):
    out = (factorial(n-l-1) / (2*n*factorial(n+l)))**0.5
    out = out * (2/(a*n))**1.5
    x_array = np.multiply(r_array, 2/(a*n))
    out = np.multiply(out,np.power(x_array,l))
    out = np.multiply(out,np.exp(np.multiply(-0.5,x_array)))
    out = np.multiply(out,gamma(x_array,l,n))
    return out

def Y1(theta, phi, m, l):
    return (-1)**m * ((2*l +1)/(4 * np.pi) * (factorial(l-m)/factorial(l+m)))**0.5 * P(m,l,np.cos(theta)) * np.exp(0+1j * m*phi)

def omega(theta,phi,l,m):
    if m == 0:
        return Y1(theta, phi, 0, l)
    elif m < 0:
        return Y1(theta, phi, -m, l) - Y1(theta, phi, m, l)
    else:
        return Y1(theta, phi, m, l) + Y1(theta, phi, -m, l)

def psi(r,theta,phi,n,l,m):
    global M,mu,a
    M = A*u
    mu = (m_e*M)/(m_e+M)
    a = (m_e*a_0)/(mu*Z)
    return np.multiply(R(r, n, l), omega(theta,phi,l,m))


r_array=np.linspace(0, 4, 200)      #in Angstroms

plt.plot(r_array, np.power(R(r_array,n=N,l=L),2))
plt.suptitle(f"Hydrogenic atom: Z={Z}, A={A}, n={N}, L={L}", y=0.95)
plt.xlabel("radius /Angstroms")
plt.ylabel("Probability density")
plt.show()

print("Rendering contour maps...")

def plot1(Z,L,m):
    Z1 = psi(R_ARRAY,THETA,np.pi/2,n=N,l=L,m=m)
    Z1 = Z1 * np.conjugate(Z1)
    ax = plt.gca()
    ax.set_aspect("equal")
    plt.scatter(-np.sin(THETA)*R_ARRAY,np.cos(THETA)*R_ARRAY,c=Z1,cmap="plasma")
    plt.colorbar()
    plt.suptitle(f"Hydrogenic atom: Z={Z}, A={A}, M={m}, N={N}, L={L}", y=0.95)
    plt.xlabel("x /Angstroms")
    plt.show()

def plot2(Z,L,m):
    Z1 = psi(R_ARRAY,np.pi/2,THETA,n=N,l=L,m=m)
    Z1 = Z1 * np.conjugate(Z1)
    ax = plt.gca()
    ax.set_aspect("equal")
    plt.scatter(np.cos(THETA)*R_ARRAY,-np.sin(THETA)*R_ARRAY,c=Z1,cmap="plasma")
    plt.colorbar()
    plt.suptitle(f"Hydrogenic atom: Z={Z}, A={A}, M={m}, N={N}, L={L}", y=0.95)
    plt.xlabel("x /Angstroms")
    plt.show()

def inv(Z):
    low = Z<0.9
    high = Z>0.9
    Z[low] = Z[low]*0 + 0.000001
    Z[high] = Z[high]*0 + 0.2
    return Z

def plot3(Z,L,m,R_ARRAY,THETA,PHI):
    cutoff=0.15
    Z1 = psi(R_ARRAY,THETA,PHI,n=N,l=L,m=m)
    Z1 = Z1 * np.conjugate(Z1)
    z_max = np.max(Z1)
    Z1 = Z1/z_max
    R_ARRAY=R_ARRAY[Z1>cutoff]
    THETA=THETA[Z1>cutoff]
    PHI=PHI[Z1>cutoff]
    ax = plt.axes(projection="3d")
    ax.set_aspect("equal")
    ax.scatter(np.cos(PHI)*R_ARRAY,np.sin(THETA)*np.sin(PHI)*R_ARRAY,np.sin(PHI)*np.cos(THETA)*R_ARRAY,c=Z1[Z1>cutoff],cmap="plasma",alpha=inv(Z1[Z1>cutoff]),vmin=0,vmax=1)
    plt.suptitle(f"Hydrogenic atom: Z={Z}, A={A}, M={m}, N={N}, L={L}", y=0.95)
    plt.xlabel("x /Angstroms")
    plt.show()

Z,A = 1,1
r_array=np.linspace(0, 10, 200)      #in Angstroms
theta_array = np.linspace(-np.pi,np.pi,200)

THETA, R_ARRAY = np.meshgrid(theta_array, r_array)

L,m,N = 2,0,3

plot1(Z,L,m)
plot2(Z,L,m)

r_array=np.linspace(0, 10, 200)      #in Angstroms
theta_array = np.linspace(-np.pi,np.pi, 200)
R_ARRAY,THETA,PHI = np.meshgrid(r_array,theta_array,theta_array)

plot3(Z,L,m,R_ARRAY,THETA,PHI)
