import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from motion import gyration, gyration_loop
from motion import drift_exb, drift_exb_loop
from motion import drift_gradb, drift_gradb_loop


#Particella scelta per la simulazione
B=0.015 #T    su z
E=5001 #N/C    su x
dB=0.2 #T/m    su y
print('\nSi digiti un numero per sceglie la particella da simulare: \n 1) elettrone 2) protone 3) muone+ 4) muone-')
while True:
    scelta=int(input('>>> '))
    if(scelta==1):
        q=-1.602*10**(-19)
        m=9.1093837015*10**(-31)
        B=0.015 #T    su z
        E=6000 #N/C    su x
        dB=25 #T/m    su y
        break
    elif(scelta==2):
        q=1.602*10**(-19)
        m=1.6726231*10**(-27)
        B=0.015 #T    su z
        E=6000 #N/C    su x
        dB=0.05 #T/m    su y
        break
    elif(scelta==3):
        q=1.602*10**(-19)
        m=1.8835327*10**(-28)
        break
    elif(scelta==4):
        q=-1.602*10**(-19)
        m=1.8835327*10**(-28)
        break
    else:
        print('Risposta non valida. Riprovare.')
print('\nLa particella scelta è tale che \n q={:} C \n m={:} kg'.format(q,m))
v0_x=5*10**5
v0_y=0 
v0_z=8*10
print('La velocità iniziale vale v=({:}, {:}, {:}) m/s'.format(v0_x, v0_y, v0_z))
print('Le configurazioni disponibili di campo sono le seguenti \n 1) B={:}T 2) E={:}N/C 3) dB={:}T/m'.format(B,E,dB))

#Inizio della simulazione
N=int(input('\nInserire il numero di step compiuti dalla particella (1 giro ogni 100): '))

#PARTE 1: singola particella
print('\n-------------------- SIMULAZIONE PARTICELLA SINGOLA --------------------')
si='y'
while (si=='Y')|(si=='y'):
    simul=int(input('\nSi scelga la configurazione di campi preferita: \n 1) Campo magnetico B uniforme lungo z (moto: gyration); \n 2) Campo magnetico B uniforma lungo z ed elettrico E uniforme lungo x (moto: drift ExB); \n 3) Campo magnetico B uniforme lungo z e gradiente lungo y (moto: drift dB) \n >>> '))
    if(simul==1):
        p_g=gyration(B, q, m, v0_x, v0_y, v0_z, N)
    elif(simul==2):
        p_exb=drift_exb(E, B, q, m, v0_x, v0_y, v0_z, N)
    elif(simul==3):
        p_gradb=drift_gradb(dB, B, q, m, v0_x, v0_y, v0_z, N)
    else:
        print('Risposta non valida.')
    si=input('\nRispondere con y/Y per ritentare \n <<< ')
color_t=np.linspace(0, 1, N)

#PARTE 2: velocità iniziale random
print('\n -------------------- SIMULAZIONE PARTICELLE A VELOCITÀ INIZIALE RANDOM --------------------')
p=int(input('Quante particelle si desidera generare? '))
particles_v0=np.empty((0,3))
for i in range(0,p):
    particles_v0=np.append(particles_v0, [np.random.uniform(low=-5*10**5, high=5*10**5, size=3)], axis=0)

si='y'
while (si=='Y')|(si=='y'):
    particella=np.empty((0, N))
    simul=int(input('\nSi scelga la configurazione di campi preferita: \n 1) Campo magnetico B uniforme lungo z (moto: gyration); \n 2) Campo magnetico B uniforma lungo z ed elettrico E uniforme lungo x (moto: drift ExB); \n 3) Campo magnetico B uniforme lungo z e gradiente lungo y (moto: drift dB) \n >>> '))
    if(simul==1):
        for i in range(0, p):
            particella=np.append(particella, gyration_loop(B, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
    elif(simul==2):
        for i in range(0, p):
            particella=np.append(particella, drift_exb_loop(E, B, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
    elif(simul==3):
        for i in range(0, p):
            particella=np.append(particella, drift_gradb_loop(dB, B, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
    else:
        print('Risposta non valida.')
        break

    print('Risultato della simulazione multipla')
    fig = plt.figure(figsize = (9, 9))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettorie tridimensionali".format(E,B), fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    for i in range(0,p*3,3):
        ax.scatter(particella[i,:], particella[i+1,:], particella[i+2,:], marker='.', label='Particella {:}'.format(int(i/3)))
    ax.set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()
    si=input('\nRispondere con y/Y per ritentare \n <<< ')

print('\nSimulazione completata.')
