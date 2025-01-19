#import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Vectorial fields", fontsize = 20)
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)
ax.set_zlabel("z", fontsize = 16)
x, y, z = np.meshgrid(np.linspace(-7, 7, 15), np.linspace(-7, 7, 15), np.linspace(-7, 7, 15))
k=0.9
dB=0.8
Bx = dB*np.cos(k*z)
By = dB*np.sin(k*z)
Bz = 0.01
ax.quiver(x, y, z, Bx, By, Bz, color='red')
ax.set_title('Vector Field')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
