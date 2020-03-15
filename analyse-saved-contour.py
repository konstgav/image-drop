import numpy as np
import matplotlib.pyplot as plt
import analysis

def GenerateRandomData():
    N = 30000
    phi = 2*np.pi*np.random.random_sample(N) - np.pi
    y = 1.+np.cos(4*phi)+np.sin(10*phi)
    data = np.empty((N,2),float)
    data[:,0] = y*np.cos(phi)
    data[:,1] = y*np.sin(phi)
    return data

def AverageNUFFT(dirname, NumPic, startFileNum, MaxFreq):
    Fouriers = []
    for i in range(NumPic):
        filename = './' + dirname + '/contour'+(str)(startFileNum+i) + '.txt'
        print('Process ' + filename)
        data = np.loadtxt(filename)
        Fouriers.append(analysis.ApplyFINUFFT(data, False, MaxFreq, None))
    print('Start FFT averaging ...')
    averFourier = np.empty(MaxFreq)
    for j in range(MaxFreq):
        averFourier[j] = 0
        for i in range(NumPic):
            N = len(Fouriers[i])
            averFourier[j] += abs(Fouriers[i][N//2+j+1])
        averFourier[j] /= NumPic
    print('Finish FFT averaging ...')    
    plt.xlabel('Frequency-1')
    plt.ylabel('|A|')
    plt.title('Average Fourier Descriptors')
    plt.plot(averFourier)
    #plt.show()
    plt.savefig(dirname + 'FFT.png')
    return 1

AverageNUFFT('fractal2', NumPic = 350, startFileNum = 500, MaxFreq = 600)


#data = np.loadtxt('./fractal1/contour910.txt')
#data = GenerateRandomData()
#analysis.ApplyFINUFFT(data)