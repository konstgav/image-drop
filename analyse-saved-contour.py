import numpy as np
import matplotlib.pyplot as plt
import analysis

#data = np.loadtxt('./fractal1/contour910.txt')
data = np.empty((1000,2),float)
for i in range(1000):
    data[i,0] = (100.+5.*np.sin(2*i*np.pi/100)+2.*np.sin(2*i*np.pi/10))*np.cos(2*i*np.pi/1000)
    data[i,1] = (100.+5.*np.sin(2*i*np.pi/100)+2.*np.sin(2*i*np.pi/10))*np.sin(2*i*np.pi/1000)
analysis.GetFourierDescriptors(data)