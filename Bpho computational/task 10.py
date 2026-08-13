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
    return np.multiply(R(r, n, l), omega(theta,phi,l,m))


r_array=np.linspace(0, 4, 1000)      #in Angstroms

plt.plot(r_array, np.power(R(r_array,n=N,l=L),2))
plt.suptitle(f"Hydrogenic atom: Z={Z}, A={A}, n={N}, L={L}", y=0.95)
plt.xlabel("radius /Angstroms")
plt.ylabel("Probability density")
plt.show()

print("Rendering contour maps...")
theta_array = np.linspace(-np.pi,np.pi,1000)
THETA, R_ARRAY = np.meshgrid(theta_array, r_array)

def plot1(Z,L,m):
    Z1 = psi(R_ARRAY,THETA,np.pi/2,n=N,l=L,m=0)
    Z1 = Z1 * np.conjugate(Z1)
    plt.contour(-np.sin(THETA)*R_ARRAY,np.cos(THETA)*R_ARRAY,Z1,1000)
    plt.show()

def plot2(Z,L,m):
    Z1 = psi(R_ARRAY,np.pi/2,THETA,n=N,l=L,m=0)
    Z1 = Z1 * np.conjugate(Z1)
    plt.contour(-np.sin(THETA)*R_ARRAY,np.cos(THETA)*R_ARRAY,Z1,1000)
    plt.show()

Z,L,m = 1,2,0
plot1(Z,L,m)
plot2(Z,L,m)
Z,L,m = 1,3,2
plot1(Z,L,m)
plot2(Z,L,m)









