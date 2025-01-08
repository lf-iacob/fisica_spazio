import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import cm

'''
Script in cui implemento la gyration ed i drift richiesti con le formule del professor Tomassetti,
cioè dove la velocità iniziale è tutta sull'asse x e v_ortogonale è definito come il teorema di
Pitagora applicato su vx_0 e vy_0 (cioè è solo vx_0 apparently).
'''


''' IMPLEMENTAZIONE delle funzioni '''

def gyration(B, q, m, v0_x, v0_y, v0_z, N):
    print('---------- GYRATION ----------')
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        vxi=v_ort*np.cos(omega_c*j*t)
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)
        vx=np.append(vx, vxi)
        vy=np.append(vy, vyi)
        xt=xt+vxi*t
        yt=yt+vyi*t
        x=np.append(x, xt)
        y=np.append(y, yt)
    z=vz*time
        
    #TO CHECK THE VELOCITY
    print('Rispondere alle domande con y/Y')
    vis_vel=input('Visualizzare i grafici di velocità? ')
    if((vis_vel=='y') | (vis_vel=='Y')):
        print('GRAFICI DI VELOCITÀ')
        print('Velocità ortogonale')
        plt.figure(figsize=(8,8))
        plt.plot(vx, vy, marker='.', color='mediumblue')
        plt.title('v_ortogonale (t)')
        plt.xlabel('vx (m/s)')
        plt.ylabel('vy (m/s)')
        plt.show()
        print('Velocità: andamento nel tempo')
        fig, ax=plt.subplots(1, 3, figsize=(15,6))
        fig.suptitle('Leggi di velocità su ogni dimensione', fontsize=25, y=1)
        ax[0].set_title('VX', fontsize=15)
        ax[0].plot(time, vx, color='mediumblue')
        ax[0].grid(linestyle=':')
        ax[0].set_xlabel('Tempo (s)', fontsize=10)
        ax[0].set_ylabel('vx(t) (m)', fontsize=10)
        ax[1].set_title('VY', fontsize=15)
        ax[1].plot(time, vy, color='purple')
        ax[1].grid(linestyle=':')
        ax[1].set_xlabel('Tempo (s)', fontsize=10)
        ax[1].set_ylabel('vy(t) (m)', fontsize=10)
        ax[2].set_title('VZ', fontsize=15)
        ax[2].plot(time, vz, color='orangered')
        ax[2].grid(linestyle=':')
        ax[2].set_xlabel('Tempo (s)', fontsize=10)
        ax[2].set_ylabel('vz(t) (m)', fontsize=10)
        plt.show()
        print('Visualizzazione tridimensionale del vettore velocità')
        fig = plt.figure(figsize = (10,10))
        ax = fig.add_subplot(projection = '3d')
        ax.set_title("Velocità tridimensionale", fontsize = 20)
        ax.set_xlabel("vx (m/s)", fontsize = 16)
        ax.set_ylabel("vy (m/s)", fontsize = 16)
        ax.set_zlabel("vz (m/s)", fontsize = 16)
        ax.scatter(vx, vy, vz, marker='.', c=vz, cmap='plasma')
        plt.show()

    #TO CHECK THE POSITION
    vis_pos=input('Visualizzare i grafici di posizione? ')
    if((vis_pos=='y')| (vis_pos=='Y')):
        print('GRAFICI DI POSIZIONE')
        print('Proiezione ortogonale della traiettoria')
        plt.figure(figsize=(8,8))
        plt.plot(x, y, marker='.', color='black')
        plt.title('Traiettoria ortogonale (t)')
        plt.xlabel('x (m/s)')
        plt.ylabel('y (m/s)')
        plt.show()
        print('Leggi orarie')
        fig, ax=plt.subplots(1, 3, figsize=(15,6))
        fig.suptitle('Leggi orarie', fontsize=25, y=1)
        ax[0].set_title('X', fontsize=15)
        ax[0].plot(time, x, color='mediumseagreen')
        ax[0].grid(linestyle=':')
        ax[0].set_xlabel('Tempo (s)', fontsize=10)
        ax[0].set_ylabel('x(t) (m)', fontsize=10)
        ax[1].set_title('Y', fontsize=15)
        ax[1].plot(time, y, color='lightseagreen')
        ax[1].grid(linestyle=':')
        ax[1].set_xlabel('Tempo (s)', fontsize=10)
        ax[1].set_ylabel('y(t) (m)', fontsize=10)
        ax[2].set_title('Z', fontsize=15)
        ax[2].plot(time, z, color='teal')
        ax[2].grid(linestyle=':')
        ax[2].set_xlabel('Tempo (s)', fontsize=10)
        ax[2].set_ylabel('z(t) (m)', fontsize=10)
        plt.show()
    print('Visualizzazione tridimensionale della traiettoria della particella')
    fig = plt.figure(figsize = (10, 10))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettoria tridimensionale", fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    ax.scatter(x, y, z, c=time, cmap='plasma')
    plt.plot(x, y, z, color='black', lw=0.7)
    plt.show()
    
    step=np.array([x,y,z])
    return step


def drift_exb(E, B, q, m, v0_x, v0_y, v0_z, N):
    print('---------- DRIFT EXB ----------')
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    field=E/B
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vz=np.full(N, v0_z)
    vx=np.empty(0)
    vy=np.empty(0)
    xt=0
    yt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        vxi=v_ort*np.cos(omega_c*j*t)
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)-field
        vx=np.append(vx, vxi)
        vy=np.append(vy, vyi)
        xt=xt+vxi*t
        yt=yt+vyi*t
        x=np.append(x, xt)
        y=np.append(y, yt)
    z=vz*time
        
    #TO CHECK THE VELOCITY
    print('Rispondere alle domande con y/Y')
    vis_vel=input('Visualizzare i grafici di velocità? ')
    if((vis_vel=='y') | (vis_vel=='Y')):
        print('GRAFICI DI VELOCITÀ')
        print('Velocità ortogonale')
        plt.figure(figsize=(8,8))
        plt.plot(vx, vy, marker='.', color='mediumblue')
        plt.title('v_ortogonale (t)')
        plt.xlabel('vx (m/s)')
        plt.ylabel('vy (m/s)')
        plt.axis('equal')
        plt.show()
        print('Velocità: andamento nel tempo')
        fig, ax=plt.subplots(1, 3, figsize=(15,6))
        fig.suptitle('Leggi di velocità su ogni dimensione', fontsize=25, y=1)
        ax[0].set_title('VX', fontsize=15)
        ax[0].plot(time, vx, color='mediumblue')
        ax[0].grid(linestyle=':')
        ax[0].set_xlabel('Tempo (s)', fontsize=10)
        ax[0].set_ylabel('vx(t) (m)', fontsize=10)
        ax[1].set_title('VY', fontsize=15)
        ax[1].plot(time, vy, color='purple')
        ax[1].grid(linestyle=':')
        ax[1].set_xlabel('Tempo (s)', fontsize=10)
        ax[1].set_ylabel('vy(t) (m)', fontsize=10)
        ax[2].set_title('VZ', fontsize=15)
        ax[2].plot(time, vz, color='orangered')
        ax[2].grid(linestyle=':')
        ax[2].set_xlabel('Tempo (s)', fontsize=10)
        ax[2].set_ylabel('vz(t) (m)', fontsize=10)
        plt.show()
        print('Visualizzazione tridimensionale del vettore velocità')
        fig = plt.figure(figsize = (10,10))
        ax = fig.add_subplot(projection = '3d')
        ax.set_title("Velocità tridimensionale", fontsize = 20)
        ax.set_xlabel("vx (m/s)", fontsize = 16)
        ax.set_ylabel("vy (m/s)", fontsize = 16)
        ax.set_zlabel("vz (m/s)", fontsize = 16)
        ax.scatter(vx, vy, vz, marker='.', c=vz, cmap='plasma')
        ax.set_aspect('equal')
        ax.set_zlim(min(vz), max(vz))
        plt.show()

    #TO CHECK THE POSITION
    vis_pos=input('Visualizzare i grafici di posizione? ')
    if((vis_pos=='y') | (vis_pos=='Y')):
        print('GRAFICI DI POSIZIONE')
        print('Proiezione ortogonale della traiettoria')
        plt.figure(figsize=(8,8))
        plt.plot(x, y, marker='.', color='black')
        plt.title('Traiettoria ortogonale (t)')
        plt.xlabel('x (m/s)')
        plt.ylabel('y (m/s)')
        plt.axis('equal')
        plt.show()
        print('Leggi orarie')
        fig, ax=plt.subplots(1, 3, figsize=(15,6))
        fig.suptitle('Leggi orarie', fontsize=25, y=1)
        ax[0].set_title('X', fontsize=15)
        ax[0].plot(time, x, color='mediumseagreen')
        ax[0].grid(linestyle=':')
        ax[0].set_xlabel('Tempo (s)', fontsize=10)
        ax[0].set_ylabel('x(t) (m)', fontsize=10)
        ax[1].set_title('Y', fontsize=15)
        ax[1].plot(time, y, color='lightseagreen')
        ax[1].grid(linestyle=':')
        ax[1].set_xlabel('Tempo (s)', fontsize=10)
        ax[1].set_ylabel('y(t) (m)', fontsize=10)
        ax[2].set_title('Z', fontsize=15)
        ax[2].plot(time, z, color='teal')
        ax[2].grid(linestyle=':')
        ax[2].set_xlabel('Tempo (s)', fontsize=10)
        ax[2].set_ylabel('z(t) (m)', fontsize=10)
        plt.show()
    print('Visualizzazione tridimensionale della traiettoria della particella')
    fig = plt.figure(figsize = (10, 10))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettoria tridimensionale", fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    ax.scatter(x, y, z, c=time, cmap='viridis')
    plt.plot(x, y, z, color='black', lw=0.7)
    ax.set_aspect('equal', adjustable='box')
    ax.set_zlim(min(z), max(z))
    plt.show()

    step=np.array([x,y,z])
    return step


def drift_gradb(grad, B, q, m, v0_x, v0_y, v0_z, N):
    print('---------- DRIFT GRAD_B ----------')
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    field=(q/abs(q))*((grad*v_ort**2)/(2*omega_c*B))
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        vxi=v_ort*np.cos(omega_c*j*t)-field
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)
        vx=np.append(vx, vxi)
        vy=np.append(vy, vyi)
        xt=xt+vxi*t
        yt=yt+vyi*t
        x=np.append(x, xt)
        y=np.append(y, yt)
    z=vz*time
        
    #TO CHECK THE VELOCITY
    print('Rispondere alle domande con y/Y')
    vis_vel=input('Visualizzare i grafici di velocità? ')
    if((vis_vel=='y') | (vis_vel=='Y')):
        print('GRAFICI DI VELOCITÀ')
        print('Velocità ortogonale')
        plt.figure(figsize=(8,8))
        plt.plot(vx, vy, marker='.', color='mediumblue')
        plt.title('v_ortogonale (t)')
        plt.xlabel('vx (m/s)')
        plt.ylabel('vy (m/s)')
        plt.axis('equal')
        plt.show()
        print('Velocità: andamento nel tempo')
        fig, ax=plt.subplots(1, 3, figsize=(15,6))
        fig.suptitle('Leggi di velocità su ogni dimensione', fontsize=25, y=1)
        ax[0].set_title('VX', fontsize=15)
        ax[0].plot(time, vx, color='mediumblue')
        ax[0].grid(linestyle=':')
        ax[0].set_xlabel('Tempo (s)', fontsize=10)
        ax[0].set_ylabel('vx(t) (m)', fontsize=10)
        ax[1].set_title('VY', fontsize=15)
        ax[1].plot(time, vy, color='purple')
        ax[1].grid(linestyle=':')
        ax[1].set_xlabel('Tempo (s)', fontsize=10)
        ax[1].set_ylabel('vy(t) (m)', fontsize=10)
        ax[2].set_title('VZ', fontsize=15)
        ax[2].plot(time, vz, color='orangered')
        ax[2].grid(linestyle=':')
        ax[2].set_xlabel('Tempo (s)', fontsize=10)
        ax[2].set_ylabel('vz(t) (m)', fontsize=10)
        plt.show()
        print('Visualizzazione tridimensionale del vettore velocità')
        fig = plt.figure(figsize = (10,10))
        ax = fig.add_subplot(projection = '3d')
        ax.set_title("Velocità tridimensionale", fontsize = 20)
        ax.set_xlabel("vx (m/s)", fontsize = 16)
        ax.set_ylabel("vy (m/s)", fontsize = 16)
        ax.set_zlabel("vz (m/s)", fontsize = 16)
        ax.scatter(vx, vy, vz, marker='.', c=vz, cmap='plasma')
        ax.set_aspect('equal')
        ax.set_zlim(min(vz), max(vz))
        plt.show()

    #TO CHECK THE POSITION
    vis_pos=input('Visualizzare i grafici di posizione? ')
    if((vis_pos=='y') | (vis_pos=='Y')):
        print('GRAFICI DI POSIZIONE')
        print('Proiezione ortogonale della traiettoria')
        plt.figure(figsize=(8,8))
        plt.plot(x, y, marker='.', color='black')
        plt.title('Traiettoria ortogonale (t)')
        plt.xlabel('x (m/s)')
        plt.ylabel('y (m/s)')
        plt.axis('equal')
        plt.show()
        print('Leggi orarie')
        fig, ax=plt.subplots(1, 3, figsize=(15,6))
        fig.suptitle('Leggi orarie', fontsize=25, y=1)
        ax[0].set_title('X', fontsize=15)
        ax[0].plot(time, x, color='mediumseagreen')
        ax[0].grid(linestyle=':')
        ax[0].set_xlabel('Tempo (s)', fontsize=10)
        ax[0].set_ylabel('x(t) (m)', fontsize=10)
        ax[1].set_title('Y', fontsize=15)
        ax[1].plot(time, y, color='lightseagreen')
        ax[1].grid(linestyle=':')
        ax[1].set_xlabel('Tempo (s)', fontsize=10)
        ax[1].set_ylabel('y(t) (m)', fontsize=10)
        ax[2].set_title('Z', fontsize=15)
        ax[2].plot(time, z, color='teal')
        ax[2].grid(linestyle=':')
        ax[2].set_xlabel('Tempo (s)', fontsize=10)
        ax[2].set_ylabel('z(t) (m)', fontsize=10)
        plt.show()
    print('Visualizzazione tridimensionale della traiettoria della particella')
    fig = plt.figure(figsize = (10, 10))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettoria tridimensionale", fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    ax.scatter(x, y, z, c=time, cmap='magma')
    plt.plot(x, y, z, color='black', lw=0.7)
    ax.set_aspect('equal', adjustable='box')
    ax.set_zlim(min(z), max(z))
    plt.show()

    step=np.array([x,y,z])
    return step



''' USO delle funzioni implementate '''

#Simulo il passaggio di una particella
q=-1.602*10**(-19) #C
m=9.1093837015*10**(-31) #kg
v0_x=2*10**5
v0_y=0 #le formule di Tomassetti sono così
v0_z=5*10**2

B=0.015 #T    su z
E=600 #N/C     su x
dB=25 #T/m      su y

N=int(input('Inserire il numero di step compiuti dalla particella: '))

#PROVA 1: gyration pura
p_g=gyration(B, q, m, v0_x, v0_y, v0_z, N)
p_exb=drift_exb(E, B, q, m, v0_x, v0_y, v0_z, N)
p_gradb=drift_gradb(dB, B, q, m, v0_x, v0_y, v0_z, N)
color_t=np.linspace(0, 1, N)


print('Traiettoria della particella nei vari casi')
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
ax.scatter(p_g[0,:], p_g[1,:], p_g[2,:], color='red', label='Gyration')
plt.plot(p_g[0,:], p_g[1,:], p_g[2,:], color='black', lw=0.7)
ax.scatter(p_exb[0,:], p_exb[1,:], p_exb[2,:], color='mediumseagreen', label='Drift ExB')
plt.plot(p_exb[0,:], p_exb[1,:], p_exb[2,:], color='black', lw=0.7)
ax.scatter(p_gradb[0,:], p_gradb[1,:], p_gradb[2,:], color='pink', label='Drift GradB')
plt.plot(p_gradb[0,:], p_gradb[1,:], p_gradb[2,:], color='black', lw=0.7)
ax.set_aspect('equal', adjustable='box')
ax.set_zlim(min(p_exb[2,:]), max(p_exb[2,:]))
ax.legend()
plt.show()
