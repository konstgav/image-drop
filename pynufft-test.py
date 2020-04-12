from pynufft import NUFFT_cpu, NUFFT_hsa
import numpy as np
import matplotlib.pyplot as plt

NufftObj = NUFFT_cpu()
N = 1000
#om = np.random.randn(1512,1)
#om = np.random.random_sample(N)
om = np.linspace(0,1,N)
y = 20.+np.cos(40*np.pi*om) + np.sin(100*np.pi*om) + np.sin(60*np.pi*om)
plt.plot(y)
plt.show()

Nd = (1000,)
Kd = (2000,)
Jd = (6,)
NufftObj.plan(om, Nd, Kd, Jd)

nufft_freq_data = NufftObj.forward(y)
plt.plot(abs(nufft_freq_data))
plt.show()

restore_time2 = NufftObj.solve(nufft_freq_data,'L1TVOLS', maxiter=30,rho=1)

im4,=plt.plot(np.abs(restore_time2))
plt.show()