import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#TODO: требуется рефакторинг, убрать комментарии
#TODO: передать номера файлов

def func(x, k, b):
    return k*x + b

class fractal_dimension:
    def __init__(self, fpath, start_frame, finish_frame):
        self.fpath = fpath
        self.start_frame = start_frame
        self.finish_frame = finish_frame

    def compute(self):
        with open(os.path.join(self.fpath.to_results_dir(), 'dimensions-frac.txt'), 'w') as f:
            aver, accuracy = self.average_fractal_dim(self.start_frame, self.finish_frame)
            print('Fractal dimension:')
            print(aver, accuracy)
            f.write("{:5.3f} {:5.3f} \n".format(aver, accuracy))

    def box_counting(self, data, d):
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
        N = np.sum(count)

        #display = np.zeros((x*d,y*d), int)
        #for i in range(x):
        #    for j in range(y):
        #        for p in range(d):
        #            for q in range(d):
        #                if count[i, j] == 1:
        #                    display[i*d+p, j*d+q] = 1 
        #
        #ax = plt.subplot(111) 
        #plt.plot(data[:,1]-min1, data[:,0]-min0)
        #plt.imshow(display)
        #plt.setp(ax.get_yticklabels(), visible=False)
        #plt.setp(ax.get_xticklabels(), visible=False)
        #ax.tick_params(axis='both', which='both', length=0)
        #plt.savefig('dimension2.png', dpi=300)
        #quit()
        #plt.show()
        return N

    def get_fractal_dim(self, filename):
        data = np.loadtxt(filename)
        #N = 1000
        #phi = np.linspace(-0.5, 0.5, N)
        #y = 40.+np.cos(40*np.pi*phi) + np.sin(100*np.pi*phi) + np.sin(60*np.pi*phi)
        #data = np.empty((N,2),float)
        #data[:,0] = y*np.cos(2*np.pi*phi)
        #data[:,1] = y*np.sin(2*np.pi*phi)
        deltas = np.array([4,8,16,32])
        Ns = []
        for d in deltas:
            Ns.append(self.box_counting(data, d))
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

    def average_fractal_dim(self, first_file, last_file):
        dims = np.empty(last_file - first_file, float)
        for i in range(first_file, last_file):
            filename = os.path.join(self.fpath.to_contours_dir(), 'contour' + (str)(i) + '.txt')
            dims[i-first_file] = self.get_fractal_dim(filename)
        aver = np.average(dims)
        accuracy = np.std(dims)
        return aver, accuracy