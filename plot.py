import matplotlib.pyplot as plt
import numpy as np
from math import pi 

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

#plt.yscale('log')
#plt.xscale('log')

#plt.plot(np.array(areas1))
plt.plot(np.array(areas2))
		
#plt.plot(np.array(areas1)/areas1[40])
#plt.plot(np.array(areas2)/areas2[40])
plt.show()

