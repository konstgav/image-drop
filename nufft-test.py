import numpy as np
from nfft import nfft
import matplotlib.pyplot as plt

def compute_nfft(sample_instants, sample_values):
    N = len(sample_instants)
    T = sample_instants[-1] - sample_instants[0]
    x = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    y = nfft(sample_instants, sample_values)
    y = 2.0 / N * np.abs(y[0:N // 2])
    return (x, y)

a = np.array([[1,2,3],[7,8,9],[6,5,4]])
print(a)
print(a[0,2])
a = a[a[:,2].argsort()]
print(a)

N = 1000
sample_instants = np.random.random_sample(N)
sample_instants = np.sort(sample_instants)
#sample_instants = np.linspace(-0.5,0.5,N)
sample_values = 20. + np.cos(40*np.pi*sample_instants) + np.sin(100*np.pi*sample_instants) + np.sin(60*np.pi*sample_instants)
plt.plot(sample_instants,sample_values)
plt.show()
plt.plot(abs(nfft(sample_instants, sample_values)))
plt.show()