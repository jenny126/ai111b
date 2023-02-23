import matplotlib.pyplot as plt
import numpy as np
import random
# y = a + bx

# x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
# y = np.array([2, 3, 4, 5, 6], dtype=np.float32)
x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([5, 7, 9, 11, 13], dtype=np.float32)

def predict(a, xt):
	return a[0]+a[1]*xt

def MSE(a, x, y):# 最小平方法
	total = 0
	for i in range(len(x)):
		total += (y[i]-predict(a,x[i]))**2
	return total

def loss(p):
	return MSE(p, x, y)

# p = [0.0, 0.0]
# plearn = optimize(loss, p, max_loops=3000, dump_period=1)
def f(x,p):
    return p[0]+p[1]*x
def optimize(P1):
	max_loops=10000
	failTime=0
	while (failTime<max_loops):
		pa =random.uniform(-0.1,0.1)
		pb=random.uniform(-0.1,0.1)
		P2=[P1[0]+pa,P1[1]+pb]
		if loss(P1)>loss(P2): 
			P1=P2
			failTime=0
		else:
			failTime=failTime+1

	return P1
P1=[0,0]
p = optimize(P1)

# Plot the graph
y_predicted = list(map(lambda t: p[0]+p[1]*t, x))
print('y_predicted=', y_predicted)
plt.plot(x, y, 'ro', label='Original data')#實際的y
plt.plot(x, y_predicted, label='Fitted line')#預測的y
plt.legend()
plt.show()
