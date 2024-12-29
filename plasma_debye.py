#import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#costanti
eps_0=8.8542*pow(10, -12)
k_B=1.380649*pow(10, -23)
elet=1.6021917*pow(10, -19)

#funzioni
def pot_Q(Q, x):
  return Q/(4*np.pi*eps_0*x)
def pot_plasma(Q, T, n_0, x):
  l_d=np.sqrt((eps_0*k_B*T)/(n_0*elet*elet))
  return (Q*np.exp(-x/l_d))/(4*np.pi*eps_0*x), l_d

#dati simulati
r=np.arange(8*pow(10, -6), 300*pow(10, -6), 4*pow(10, -6))
Q=4*pow(10, -19)
n_0=100*10**12
T=100
carica=pot_Q(Q, r)
plasma,l=pot_plasma(Q, T, n_0, r)

#rappresentazione grafica
plt.figure()
plt.plot(r*10**6, carica*10**3, color='mediumseagreen', label='Carica puntiforme')
plt.plot(r*10**6, plasma*10**3, color='mediumvioletred', label='Plasma perturbato')
plt.scatter(np.full(12,l*10**6), np.linspace(0, 0.43, 12), marker='|', color='orangered', label='λD')
plt.title('Potenziale elettrico φ')
plt.xlabel('r (µm)')
plt.ylabel('φ(r) (mV)')
plt.legend()
plt.grid(linestyle=':')
plt.show()
plt.legend()
plt.show()

plt.figure()
plt.plot(r*10**6, carica*10**3, color='mediumseagreen', label='Carica puntiforme')
plt.plot(r*10**6, plasma*10**3, color='mediumvioletred', label='Plasma perturbato')
plt.scatter(np.full(12,l*10**6), pow(10, np.linspace(-3.8, -0.5, 12)), marker='|', color='orangered', label='λD')
plt.title('Potenziale elettrico φ')
plt.xlabel('r (µm)')
plt.ylabel('φ(r) (mV)')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(linestyle=':')
plt.show()
