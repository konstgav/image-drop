import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a/(x-c)+b

averageAreas = []
for filename in ['yod02.txt', 'yod03.txt', 'yod06.txt', 'yod05.txt', 'yod04.txt', 'yod07.txt', 'yod08.txt']:
    data = np.loadtxt(filename)
    averageArea = sum(data)/len(data)
    averageAreas.append(averageArea)
    
times=np.array([16.5, 32.7, 49, 65.2, 74, 98.2, 116.2])
timesFine = np.linspace(10,120,100)
popt, pcov = curve_fit(func, times, np.array(averageAreas))
plt.plot(times,averageAreas,'ko',label='эксперимент')
plt.plot(timesFine, func(timesFine,*popt), 'k', label='аппроксимация')
print(popt)
plt.xlim(10,120)
plt.xlabel(r'$t, мин$')
plt.ylabel(r'$S, см^2$')
plt.legend()
plt.grid()
plt.savefig('evaporation.png', dpi=300)
plt.show()
