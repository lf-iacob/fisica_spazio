#import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

def diff_g(x, y, t):
  k=5
  return np.exp(-(x**2+y**2)/(4*k*t))/(np.sqrt(4*k*t))

x_d=np.linspace(-15, 15, 35)
y_d=np.linspace(-15, 15, 35)

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Diffusione (MHD)", fontsize = 20)
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)
ax.set_zlabel("ψ", fontsize = 16)

X,Y=np.meshgrid(x_d,y_d)
Z0=diff_g(X,Y,1)
Z1=diff_g(X,Y,2)
Z2=diff_g(X,Y,3)

#0
norm0=plt.Normalize(Z0.min(), Z0.max())
colors0=cm.Blues_r(norm0(Z0))
rcount0, ccount0, _ =colors0.shape

#1
norm1=plt.Normalize(Z1.min(), Z1.max())
colors1=cm.Greens_r(norm1(Z1))
rcount1, ccount1, _ =colors1.shape

#2
norm2=plt.Normalize(Z2.min(), Z2.max())
colors2=cm.Reds_r(norm2(Z2))
rcount2, ccount2, _ =colors2.shape

'''
surf0=ax.plot_surface(X, Y, Z0, rcount=rcount0, ccount=ccount0, facecolors=colors0, shade=False)
surf1=ax.plot_surface(X, Y, Z1, rcount=rcount1, ccount=ccount1, facecolors=colors1, shade=False)
surf2=ax.plot_surface(X, Y, Z2, rcount=rcount2, ccount=ccount2, facecolors=colors2, shade=False)
'''

ax.scatter(X,Y,Z0, c=Z0, cmap='Blues', marker='.')
ax.scatter(X,Y,Z1, c=Z1, cmap='Greens', marker='.')
ax.scatter(X,Y,Z2, c=Z2, cmap='Reds', marker='.')

'''
surf2=ax.plot_surface(X,Y,np.where(Z1<Z2,Z2,np.nan), rcount=rcount1, ccount=ccount1, facecolors=colors1, shade=False)
surf1=ax.plot_surface(X,Y,np.where(Z1>=Z2,Z1,np.nan), rcount=rcount2, ccount=ccount2, facecolors=colors2, shade=False)
'''

'''
ax.plot_wireframe(X,Y,Z0, color='red')
ax.plot_wireframe(X,Y,Z1, color='green')
ax.plot_wireframe(X,Y,Z2, color='blue')
'''

plt.show()
