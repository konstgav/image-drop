import numpy as np
import matplotlib.pyplot as plt
import finufftpy

def ProcessFrame(contour, dirname, currentFrame,needToShowFFT, MaxFreq, figFFT):
    N = contour.shape[0]
    data = np.empty((N,2),float)
    data[:,0] = contour[:,0,0]
    data[:,1] = contour[:,0,1]
    filename = './' + dirname + '/contour' + str(currentFrame) + '.txt'
    np.savetxt(filename, data)
    #TODO: Разбить на мелкие эквидистантные интервалы контур
    #GetFourierDescriptors(data)
    ApplyFINUFFT(data, needToShowFFT, MaxFreq, figFFT)
    return 1

def ApplyFINUFFT(data, needToShowFFT, MaxFreq, figFFT):
    N = data.shape[0]
    phi = np.empty(N,float)
    xc = sum(data[:,0])/N
    yc = sum(data[:,1])/N
    contour_complex = np.empty(N, dtype=complex)
    contour_complex.real = data[:, 0]
    contour_complex.imag = data[:, 1]
    for i in range(N):
        phi[i] = np.arctan2(data[i,1]-yc, data[i,0]-xc)
    
    acc = 1.e-9
    iflag = 1
    F = np.zeros([N], dtype=np.complex128)     # allocate F (modes out)
    ret = finufftpy.nufft1d1(phi, contour_complex, iflag, acc, N, F)
    if needToShowFFT:
        PlotNonuniformData(data,F,MaxFreq, figFFT)
    return F

def MakeFigureFFT():
    fig = plt.figure(figsize=(13,5))
    ax0 = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)
    return fig

def PlotNonuniformData(data,F,MaxFreq, figFFT):
    N = F.shape[0]
    ax0 = figFFT.axes[0]
    ax1 = figFFT.axes[1]
    ax0.cla()
    ax1.cla()
    ax0.set(aspect = 1, xlabel = 'x', ylabel = 'y', title = 'Contour')
    ax0.invert_yaxis()
    ax1.set(xlabel = 'Frequency-1', ylabel = '|A|', title = 'Fourier Descriptors')
    ax0.plot(data[:,0],data[:,1])
    ax1.plot(abs(F[N//2+1:N//2+MaxFreq]))
    plt.draw()
    plt.pause(0.001)
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
    degree = 400
    plt.plot(np.fft.fftfreq(len(fourier_descriptors))[2:degree], abs(fourier_descriptors[2:degree]))
    #print(fourier_descriptors)
    plt.show()
    
    return 1