import numpy as np
import matplotlib.pyplot as plt

#for creating array object
data = np.array([[2, 2], [4, 4], [6, 6], [8, 8]])

w1 = np.arange(-15, 15, 0.5)
w0=np.arange(-15,15,0.5)
print (w1)
print(w0)
z = []
y = []




def error_function():
	for i in range(len(w1)):
		result = 0
		for j in range(len(data)):
			result += (w1[i] * data[j][0] - data[j][1]) ** 2
		y.append(result)
	plt.plot(w1, y,"blue")
	plt.grid(True,which="major")
	plt.show()
	plt.ylabel('Error function')
	plt.xlabel('W1')


	#plt.grid(b=None, which='major', axis='both',color='r',linestyle=2,linewidth=2, **kwargs)



error_function()
