import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.optimize import curve_fit
import glob, os

def func(x, a, b, c):
    return a*(x-b)**0.2+c

print(os. getcwd())
datas = []
filenames = ['20feb-1.txt']
for file in filenames:
    print('Reading ', file)
    data = np.loadtxt(file)
    datas.append(data)

#Start & stop frame numbers for approximation
start = 10
stop = 200
excludeStep = 15

plt.title('Рост площади капли')
for i in range(len(datas)):
    times = 0.001*datas[i][:,0]
    areas = datas[i][:,1]
    popt, pcov = curve_fit(func, times[start:stop], areas[start:stop])
    print('Параметры аппроксимации a, b, c: ', popt)
    plt.plot(times, func(times,*popt), label='аппроксимация')
    plt.plot(times[6::excludeStep], areas[6::excludeStep], 'o', label = 'Эксперимент №'+(str)(i+1))
plt.legend(loc="best")
plt.xlabel(r'$t, c$')
plt.ylabel(r'$S, см^2$')
plt.xlim(0,300)
plt.ylim(3,4.4)
plt.grid()
plt.savefig('growth.png', dpi=300)
plt.show()
