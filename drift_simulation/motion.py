import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

'''
Modulo che implementa come funzioni accessibili da esterno i alcuni
tipi di moto a cui è sottoposta una particella carica:
- solo campo magnetico B uniforme su z (gyration);
- B e aggiunto un campo elettrico uniforme su x (drift ExB);
- B e aggiunto un suo gradiente su y (drift grad ortogonale).

Le condizioni a contorno sono tali per cui la velocità iniziale
sul piano ortogonale a B è diretta interamente lungo l'asse x. 
'''


''' SIMULAZIONE PARTICELL SINGOLA '''

def gyration(B, q, m, v0_x, v0_y, v0_z, N):
    print('---------- GYRATION ----------')
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione inizializzati
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #simulazione: aggiornamento degli array
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
        
    #VELOCITÀ
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

    #POSIZIONE
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
    
    #array di velocità e di posizione inizializzati
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vz=np.full(N, v0_z)
    vx=np.empty(0)
    vy=np.empty(0)
    xt=0
    yt=0

    #simulazione: aggiornamento array
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
        
    #VELOCITÀ
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

    #POSIZIONE
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
    
    #array di velocità e di posizione inizializzati
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #simulazione: aggiornamento array
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
        
    #VELOCITÀ
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

    #POSIZIONE
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






''' SIMULAZIONE PARTICELLE MULTIPLE '''

def gyration_loop(B, q, m, v0_x, v0_y, v0_z, N):
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione inizializzati
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #simulazione: aggiornamento degli array
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
    
    step=np.array([x,y,z])
    return step

def drift_exb_loop(E, B, q, m, v0_x, v0_y, v0_z, N):
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    field=E/B
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione inizializzati
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vz=np.full(N, v0_z)
    vx=np.empty(0)
    vy=np.empty(0)
    xt=0
    yt=0

    #simulazione: aggiornamento array
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

    step=np.array([x,y,z])
    return step

def drift_gradb_loop(grad, B, q, m, v0_x, v0_y, v0_z, N):
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    field=(q/abs(q))*((grad*v_ort**2)/(2*omega_c*B))
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione inizializzati
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #simulazione: aggiornamento array
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

    step=np.array([x,y,z])
    return step
