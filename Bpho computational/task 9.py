#task 9
import matplotlib.pyplot as plt
import numpy as np

h = 6.626070040 * 10**-34
m_e = 9.1093835611 * 10**-31
c = 2.99792458 * 10**8
e = 1.602176620898 * 10**-19

theta_array = np.linspace(0,np.pi,1000)
delta_lambda = np.multiply(h/(m_e*c), 1-np.cos(theta_array))
E_list = [50,100,200,500,1000]

def plot1(E_list):
    for E in E_list:
        Lambda = h*c / (E*1000*e)
        d_lambda = np.divide(delta_lambda,Lambda)
        plt.plot(theta_array*(180/np.pi),d_lambda, label=f"E={E}keV")
    plt.legend()
    plt.title("Compton scattering of X-ray photon off an electron")
    plt.xlabel("Photon scattering angle θ /deg")
    plt.ylabel("Δλ/λ")
    plt.grid()
    plt.show()

def plot2(E_list):
    for E in E_list:
        Lambda = h*c / (E*1000*e)
        Lambda_prime = np.add(delta_lambda,Lambda)
        v_array = np.divide(m_e*c**2,h*c/Lambda+m_e*c**2-np.divide(h*c,Lambda_prime))
        v_array = np.power(v_array, 2)
        v_array = np.power(1-v_array,0.5)
        plt.plot(theta_array*(180/np.pi),v_array, label=f"E={E}keV")
    plt.legend()
    plt.title("Compton scattering of X-ray photon off an electron")
    plt.xlabel("Photon scattering angle θ /deg")
    plt.ylabel("Electron recoil speed v/c")
    plt.grid()
    plt.show()

def plot3(E_list):
    for E in E_list:
        Lambda = h*c / (E*1000*e)
        sn = np.sin(theta_array)
        cs = np.cos(theta_array)
        t = 1 + np.subtract(np.multiply(h/(m_e*c*Lambda),1-cs), cs)
        t = np.divide(sn, t)
        t = np.arctan(t)
        plt.plot(theta_array*(180/np.pi),t*(180/np.pi), label=f"E={E}keV")
    plt.legend()
    plt.title("Compton scattering of X-ray photon off an electron")
    plt.xlabel("Photon scattering angle θ /deg")
    plt.ylabel("Electron recoil angle ϕΦ /deg")
    plt.grid()
    plt.show()
     

plot1(E_list)
plot2(E_list)
plot3(E_list)








