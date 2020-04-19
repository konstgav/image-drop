import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.optimize import curve_fit
import glob, os

def func(x, a, b, c, d):
    return a*(x-b)+c

print(os. getcwd())
datas = []
filenames = [] #['fractal1_Areas.txt', 'fractal3_Areas.txt', 'fractal6_Areas.txt', 'fractal8_Areas.txt']
for i in range (1,21):
    filenames.append('fractal{:d}_Areas.txt'.format(i))

for file in filenames:
    print('Reading ', file)
    data = np.loadtxt(file)
    datas.append(data)

for data in datas:
    data[:,0] = data[:,0] - data[0,0]

#Start & stop frame numbers for approximation
start = 1
stop = 60
excludeStep = 15

#symbols = ['o', 'P', 'v', 's']
#colors = ['r', 'g', 'b', 'm']
k = []
plt.title('Рост площади капли')
for i in range(len(datas)):
    times = 0.001*datas[i][:,0]
    areas = datas[i][:,1]
    popt, pcov = curve_fit(func, times[start:stop], areas[start:stop])
    print('Параметры аппроксимации a, b, c: ', popt)
    k.append(popt[0])
    plt.plot(times[start:stop+40], func(times,*popt)[start:stop+40], label='Аппроксимация № {:d}: k = {:4.2f} '.format(i+1, popt[0]) + r'$см^2/c$')
    plt.plot(times[::excludeStep], areas[::excludeStep], 'o', label = 'Эксперимент №'+(str)(i+1)) #symbols[i] + colors[i], 
plt.legend(loc="best")
plt.xlabel(r'$t, c$')
plt.ylabel(r'$S, см^2$')
plt.xlim(0,10)
#plt.ylim(3,4.4
plt.grid()
plt.savefig('growth.png', dpi=300)
with open('k.txt', 'w') as f:
    for item in k:
        f.write("%s\n" % item)
plt.show()
