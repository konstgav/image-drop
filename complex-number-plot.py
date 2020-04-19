import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import finufftpy

N = 1000
phi = np.linspace(-0.5, 0.5, N)
y = 20.+np.cos(40*np.pi*phi) + np.sin(100*np.pi*phi)
data = np.empty((N,2),float)
data[:,0] = y*np.cos(2*np.pi*phi)
data[:,1] = y*np.sin(2*np.pi*phi)
plt.figure(figsize=(12,5))
ax = plt.subplot(121)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.xlabel('x')
plt.ylabel('y')
ax.arrow(-24, 0, 46, 0, head_width=1, head_length=2, fc='k', ec='k')
ax.arrow(0, 24, 0, -46, head_width=1, head_length=2, fc='k', ec='k')
plt.title('Контур капли')
plt.text(23, -2, r'$x$', fontsize = 14)
plt.text(2, -23, r'$y$', fontsize = 14)
plt.text(3.5, -1.5, r'$\varphi$', fontsize = 14)
plt.text(1, -13, r'$z = x + iy$', fontsize = 14)
plt.gca().invert_yaxis()
ax.set_aspect(1)
plt.plot(data[:,0],data[:,1])
y = 19# 20.+np.cos(-40*np.pi/8) + np.sin(-100*np.pi/8)
print(y)
circle2 = plt.Circle(((int)(y*np.cos(np.pi/4)), -(int)(y*np.sin(np.pi/4))), 0.5, color='black')
plt.plot([0, (int)(y*np.cos(np.pi/4))], [0, -(int)(y*np.sin(np.pi/4))], 'k-', lw=2)
ax.add_artist(circle2)
ax1 = plt.subplot(122)

N = 50000
phi =  np.random.random_sample(N) - 0.5
y = 20.+np.cos(40*np.pi*phi) + np.sin(100*np.pi*phi)
data = np.empty((N,2),float)
data[:,0] = y*np.cos(2*np.pi*phi)
data[:,1] = y*np.sin(2*np.pi*phi)

ax1.set(xlabel = r'$n - 1$', ylabel = r'$|A|$', title = 'Дескрипторы Фурье')
phi = np.empty(N,float)
xc = sum(data[:,0])/N
yc = sum(data[:,1])/N

contour_complex = data[:, 0] - xc + 1j*(data[:, 1] - yc)
phi = np.arctan2(data[:,1]-yc, data[:,0]-xc)

acc = 1.e-9
iflag = 1
F = np.zeros([N], dtype=np.complex128)     # allocate F (modes out)
ret = finufftpy.nufft1d1(phi, contour_complex, iflag, acc, N, F)
ax1.plot(abs(F)[N//2:N//2+80])
plt.grid()
plt.savefig('test-fft.png', dpi=600)
plt.show()