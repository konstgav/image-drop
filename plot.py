import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a*x+b

data1 = np.loadtxt('003.txt')

start = 40
times = data1[:,0]/1000. # Convert from seconds in milliseconds
values = data1[:,1]

popt, pcov = curve_fit(func, times[start:], values[start:])
print(popt)
plt.title('Area dynamics')
plt.plot(times[start:], func(times,*popt)[start:], label='linear approx')
plt.plot(times[start:], values[start:], 'o', label = 'experimental data')
plt.legend()
plt.show()