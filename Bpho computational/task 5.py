#task 5
import matplotlib.pyplot as plt
import numpy as np

#parameters
levels = 14            #energy levels to plot
colours = ["#FF0000","#00FF00","#0000FF", "#FF00FF","#00FFFF"]
###

energy_levels = []
for n in range(1,levels+1):
    energy_levels.append(-13.6 * n**-2)

plt.figure(figsize=(8,5.5))
def plot1(Z, m):
    lam = 91.13/(Z**2)
    values = []
    energy = []
    for n in range(m+1,levels+1):
        values.append(lam * (m**-2 - n**-2)**-1)
        energy.append(energy_levels[n-1] - energy_levels[m-1])
    plt.scatter(values, energy, marker="x", s=20, c=colours[m-1])
    return values

values = []
for m in range(1,5+1):
    values.append(plot1(1,m))

plt.suptitle("Bohr model of Hydrogenic atom photon emissions: Z = 1", y=0.95)
plt.xlabel("λ /nm")
plt.ylabel("Photon energy /eV")
plt.legend(["Lyman","Balmer","Pashcen","Brackett","Pfund"])

for i in range(len(values)):
    plt.vlines(x=values[i], ymin=0, ymax=13.6, color=colours[i], lw=.5, ls="--")

plt.show()
