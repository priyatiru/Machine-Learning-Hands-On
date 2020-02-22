import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,100)
y = 2*x+1
w1=np.linspace(-10,10,0.5)
w0=np.linspace(-10,10,0.5)
W0,W1=np.meshgrid(wo,w1)
l=0
it=len(x)
for i in range(it):
	l+=(W1*x[i]+W0-y[i])**2
plt.plot(x, y, '-r', label='y=2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.scatter(x,y)
plt.show()
