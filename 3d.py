import  numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

m=1
x=np.linspace(1,10,10)
y=m*x+2

w1=np.linspace(-2,4,10)
w0=np.linspace(-2,4,10)
W0,W1=np.meshgrid(w0,w1)

l=0
it=len(x)
for i in range(it):
    l+=(W1*x[i]+W0-y[i])**2

plt.contour(W0,W1,l,levels = [i for i in np.arange(-200,200,60)])
#plt.show()
fig=plt.figure()
ax=plt.axes(projection='3d')

ax.plot_surface(W0,W1,l,cmap='viridis', edgecolor='none')
