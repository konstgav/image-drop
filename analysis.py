import numpy as np
import matplotlib.pyplot as plt

def ProcessFrame(contour, dirname, currentFrame):
    N = contour.shape[0]
    data = np.empty((N,2),float)
    data[:,0] = contour[:,0,0]
    data[:,1] = contour[:,0,1]
    filename = './' + dirname + '/contour' + str(currentFrame) + '.txt'
    np.savetxt(filename, data)
    #TODO: Разбить на мелкие эквидистантные интервалы контур
    GetFourierDescriptors(data)
    return 1

def GetFourierDescriptors(data):
    N = data.shape[0]
    contour_complex = np.empty(N, dtype=complex)
    contour_complex.real = data[:, 0]
    contour_complex.imag = data[:, 1]
    fourier_result = np.fft.fft(contour_complex)

    PlotDataWithSpectr(data,fourier_result)
    return 1

def GetRaduisFFT(data):
    N = data.shape[0]
    r = np.empty(N,float)
    xc = sum(data[:,0])/N
    yc = sum(data[:,1])/N
    #print(xc,yc)

    for i in range(N):
        r[i] = np.sqrt((xc - data[i,0])**2 + (yc - data[i,1])**2)

    A = np.fft.fft(r)
    PlotDataWithSpectr(r,A)
    return 1

def PlotDataWithSpectr(data, fourier_descriptors):
    plt.figure(figsize=(13,5))
    ax = plt.subplot(121)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Contour')
    plt.gca().invert_yaxis()
    ax.set_aspect(1)
    plt.plot(data[:,0],data[:,1])
    plt.subplot(122)
    plt.ylabel('|A|')
    plt.title('Fourier Descriptors')
    plt.xlim(0,0.15)
    degree = 800
    plt.plot(np.fft.fftfreq(len(fourier_descriptors))[2:degree], abs(fourier_descriptors[2:degree]))
    #print(fourier_descriptors)
    plt.show()
    
    return 1