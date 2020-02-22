import numpy as np
import matplotlib.pyplot as plt


data = np.array([[2, 2], [4, 4], [6, 6], [8, 8]])

x = np.arange(-15, 15, 0.5)
print (x)
y = []
z = []

def error_function_mod():
	for i in range(len(x)):
		result = 0
		for j in range(len(data)):
			result += abs(x[i] * data[j][0] - data[j][1])
		z.append(result)
	plt.plot(x, y)
	plt.show()

def error_function_square():
	for i in range(len(x)):
		result = 0
		for j in range(len(data)):
			result += abs(x[i] * data[j][0] - data[j][1]) ** 2
		y.append(result)
	plt.plot(x, z)
	plt.show()

error_function_mod()
error_function_square()
