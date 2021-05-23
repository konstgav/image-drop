import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.optimize import curve_fit
import glob, os

def func(x, a, b, c, d):
    return a*x + b
    #return a*(x-b)**0.2+c

print(os. getcwd())
datas = []
filenames = ['./konst/IMG_0471/results/areas.txt', './konst/IMG_0473/results/areas.txt', './konst/IMG_0474/results/areas.txt']

for file in filenames:
    print('Reading ', file)
    data = np.loadtxt(file)
    datas.append(data)

for data in datas:
    data[:,0] = data[:,0] - data[0,0]

#Start & stop frame numbers for approximation
start = 0
stop = 50
excludeStep = 15

symbols = ['o', 'P', 'v', 's']
colors = ['r', 'g', 'b', 'm']
plt.title('Рост площади капли')
for i in range(len(datas)):
    times = 0.001*datas[i][:,0]
    areas = datas[i][:,1]
    popt, pcov = curve_fit(func, times[start:stop], areas[start:stop])
    print('Параметры аппроксимации a, b, c: ', popt)
    plt.plot(times[start:stop], func(times,*popt)[start:stop], colors[i], label='Аппроксимация №'+(str)(i+1))
    plt.plot(times[::excludeStep], areas[::excludeStep], symbols[i] + colors[i], label = 'Эксперимент №'+(str)(i+1))
plt.legend(loc="best")
plt.xlabel(r'$t, c$')
plt.ylabel(r'$S, см^2$')
#plt.xlim(0,300)
#plt.ylim(3,4.4
plt.grid()
plt.savefig('growth.png', dpi=300)
plt.show()
