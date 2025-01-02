#Velocità
def v(v0, t, tau):
  return v0*(1-np.e**(-t/tau))
t=np.linspace(0, 10, 20)
tau=1.8
v0=4
v=v(v0, t, tau)
plt.figure(figsize=(7,4))
plt.plot(t, v, color='mediumseagreen')
plt.scatter(t, np.full(20, v0), color='mediumvioletred', marker='_', lw=3)
plt.title('Velocità')
plt.xlabel('t (s)')
plt.ylabel('v(t) (m/s)')
plt.grid(linestyle=':')
plt.show()

#Conducibilità
def sigma(max, chi, rap):
  return max/(1+rap*((1-chi)/chi))
max_s=15
chi_s=np.linspace(0.2, 1, 16)
rap_s=0.01
s=sigma(max_s, chi_s, rap_s)
plt.figure(figsize=(7,4))
plt.plot(chi_s, s, color='orangered')
plt.scatter(chi_s, np.full(16, max), color='lightseagreen', marker='_', lw=3)
plt.title('Conducibilità')
plt.xlabel('χ')
plt.ylabel('σ* (S/m)')
plt.grid(linestyle=':')
plt.show()
