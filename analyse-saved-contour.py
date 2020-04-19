import numpy as np
import matplotlib.pyplot as plt
import analysis
import nfft

def GenerateRandomData():
    N = 10000
    phi = np.random.random_sample(N) - 0.5
    y = 10.+np.cos(40*np.pi*phi) + np.sin(100*np.pi*phi) + np.sin(60*np.pi*phi)
    data = np.empty((N,2),float)
    data[:,0] = y*np.cos(2*np.pi*phi)
    data[:,1] = y*np.sin(2*np.pi*phi)
    return data

def GenerateUniformDataTest():
    N = 1000
    phi = np.linspace(-0.5, 0.5, N)
    y = 20.+np.cos(40*np.pi*phi) + np.sin(100*np.pi*phi)
    data = np.empty((N,2),float)
    data[:,0] = y*np.cos(2*np.pi*phi)
    data[:,1] = y*np.sin(2*np.pi*phi)
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

#AverageNUFFT('fractal2', NumPic = 350, startFileNum = 500, MaxFreq = 600)
#data = np.loadtxt('./fractal1/contour910.txt')
#data = GenerateUniformDataTest()
data = GenerateRandomData()
analysis.ApplyFINUFFT(data, 'True', 60, analysis.MakeFigureFFT())
analysis.Apply_nfft(data, 'True', 60, analysis.MakeFigureFFT())
input("Press Enter to continue...")