import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*(x-c)**0.5+b

s = pi*97**2/4.*(5/220)**2
print(s)

areas1 = []
areas2 = []
with open('001.txt', 'r') as f:
	for line in f:
		area = (float)(line)
		areas1.append(area)

with open('002.txt', 'r') as f:
	for line in f:
		area = (float)(line)
		areas2.append(area)

radius = np.array(areas2)**0.5/np.sqrt(np.pi)
start = 25
x = np.linspace(0,radius.size-1,radius.size)
popt, pcov = curve_fit(func, x[start:], radius[start:])
print(popt)
plt.plot(func(x,*popt),label='square approx')
plt.plot(radius)
plt.show()