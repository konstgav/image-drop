import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, k, b):
    return k*x + b

def box_counting(data, d):
    min0 = np.amin(data[:,0])
    max0 = np.amax(data[:,0])
    min1 = np.amin(data[:,1])
    max1 = np.amax(data[:,1])
    leng = data.shape[0]
    x = (int)((max0-min0)/d+1)
    y = (int)((max1-min1)/d+1)
    count = np.zeros((x,y), int)
    for i in range(leng):
        num0 = (int)((data[i,0]-min0)/d)
        num1 = (int)((data[i,1]-min1)/d)
        if count[num0, num1] == 0:
            count[num0, num1] = 1

    display = np.zeros((x*d,y*d), int)
    for i in range(x):
        for j in range(y):
            for p in range(d):
                for q in range(d):
                    if count[i, j] == 1:
                        display[i*d+p, j*d+q] = 1 

    ax = plt.subplot(111) 
    plt.plot(data[:,1]-min1, data[:,0]-min0)
    N = np.sum(count)
    plt.imshow(display)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.setp(ax.get_xticklabels(), visible=False)
    ax.tick_params(axis='both', which='both', length=0)
    plt.savefig('dimension2.png', dpi=300)
    quit()
    plt.show()
    return N

def get_fractal_dim(filename):
    data = np.loadtxt(filename)
    #N = 1000
    #phi = np.linspace(-0.5, 0.5, N)
    #y = 40.+np.cos(40*np.pi*phi) + np.sin(100*np.pi*phi) + np.sin(60*np.pi*phi)
    #data = np.empty((N,2),float)
    #data[:,0] = y*np.cos(2*np.pi*phi)
    #data[:,1] = y*np.sin(2*np.pi*phi)
    deltas = np.array([32,4,8,16,32])
    Ns = []
    for d in deltas:
        Ns.append(box_counting(data, d))
    Ns = np.array(Ns)
    popt, pcov = curve_fit(func, np.log(1./deltas), np.log(Ns))
    dim = popt[0]
    last =len(deltas)-1
    #plt.plot(np.log(1./np.array([2,4,8,16,32,64])), func(np.log(1./np.array([2,4,8,16,32,64])),*popt), label = 'аппроксимация')
    #plt.plot(np.log(1./deltas), np.log(Ns),'o', label = 'эксперимент') 
    #plt.xlabel(r'$log(1/\delta)$')
    #plt.ylabel(r'$log(N(\delta))$')
    #plt.legend()
    #plt.xlim(-4,-1)
    #plt.ylim(4,8)
    #plt.grid()
    #plt.savefig('dimension1.png', dpi=300)
    #quit()
    #dim = (np.log(Ns[last]) - np.log(Ns[0]))/(np.log(1./deltas[last]) - np.log(1./deltas[0]))
    return dim

def average_fractal_dim(dirname, first_file, last_file):
    dims = np.empty(last_file - first_file, float)
    for i in range(first_file, last_file):
        filename = dirname + '/contour' + (str)(i) + '.txt'
        dims[i-first_file] = get_fractal_dim(filename)
    aver = np.average(dims)
    accuracy = np.std(dims)
    return aver, accuracy

with open('dimensions-frac.txt', 'w') as f:
    for i in range(20):
        aver, accuracy = average_fractal_dim('./fractal' + (str)(i+1), 450, 500)
        print(i, aver, accuracy)
        f.write("{:d} {:5.3f} {:5.3f} \n".format(i+1, aver, accuracy))