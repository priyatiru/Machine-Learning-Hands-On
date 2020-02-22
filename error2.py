import numpy as np
import matplotlib.pyplot as plt


#data = np.array([[2, 2], [4, 4], [6, 6], [8, 8]])

w1 = np.linspace(-5,5,20)
print (x)
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""def error_function_mod():
	for i in range(len(x)):
		result = 0
		for j in range(len(data)):
			result += abs(x[i] * data[j][0] - data[j][1])
		z.append(result)
	plt.plot(x, y)
	plt.show()"""


result = 0
for i in range(len(y)):
    result += (w1*x[i] - y[i])** 2
result
plt.plot(w1,result)
plt.xlabel('w1')
plt.ylabel('Result')
