import numpy as np
import os
import matplotlib.pyplot as plt
import finufft

def ProcessFrame(contour, fpath, currentFrame,needToShowFFT, MaxFreq, figFFT):
    N = contour.shape[0]
    data = np.empty((N,2),float)
    data[:,0] = contour[:,0,0]
    data[:,1] = contour[:,0,1]
    #TODO: изменить путь для сохранения результатов 
    filename = os.path.join(fpath.to_contours_dir(), 'contour' + str(currentFrame) + '.txt')
    np.savetxt(filename, data)
    #TODO: Разбить на мелкие эквидистантные интервалы контур
    ApplyFINUFFT(data, needToShowFFT, MaxFreq, figFFT)
    return 1

def ApplyFINUFFT(data, needToShowFFT, MaxFreq, figFFT):
    N = data.shape[0]
    if N%2 != 0:
        data = data[0:N-1,:]
        N = N-1
    phi = np.empty(N,float)
    xc = sum(data[:,0])/N
    yc = sum(data[:,1])/N

    contour_complex = data[:, 0] - xc + 1j*(data[:, 1] - yc)
    phi = np.arctan2(data[:,1]-yc, data[:,0]-xc)

    acc = 1.e-9
    iflag = 1
    F = np.zeros([N], dtype=np.complex128)     # allocate F (modes out)
    ret = finufft.nufft1d1(phi, contour_complex, None, F, acc, iflag)
    if needToShowFFT:
        PlotNonuniformData(data, F, MaxFreq, figFFT)
    return F

def MakeFigureFFT():
    fig = plt.figure(figsize=(13,5))
    ax0 = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)
    return fig

def PlotNonuniformData(data, F, MaxFreq, figFFT):
    N = F.shape[0]
    ax0 = figFFT.axes[0]
    ax1 = figFFT.axes[1]
    ax0.cla()
    ax1.cla()
    ax0.set(aspect = 1, xlabel = 'x', ylabel = 'y', title = 'Contour')
    ax0.invert_yaxis()
    ax1.set(xlabel = 'Frequency', ylabel = '|A|', title = 'Fourier Descriptors')
    ax0.plot(data[:,0],data[:,1])
    ax1.plot(abs(F)[N//2:N//2+MaxFreq])
    plt.draw()
    plt.pause(0.001)
