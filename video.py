import cv2
import numpy as np
import os
import json 
import matplotlib.pyplot as plt
import sys
import binarization
import analysis

class Video():
    def __init__(self, videoParams):
        self.filename = videoParams['filename']
        self.dirname = videoParams['dirname']
        self.frameStep = videoParams['frameStep']
        self.startFrame = videoParams['startFrame']
        self.finalFrame = videoParams['finalFrame']
        self.isSaveFrames = videoParams['isSaveFrames']
        self.needToShowContour = videoParams['needToShowContour']
        self.xmin = videoParams['xmin']
        self.xmax = videoParams['xmax']
        self.ymin = videoParams['ymin']
        self.ymax = videoParams['ymax']
        self.needToSaveAreas = videoParams['needToSaveAreas']
        self.needToShowFFT = videoParams['needToShowFFT']
        self.MaxFreq = videoParams['MaxFreq']
        self.pixelToCm = videoParams['pixelToCm']
        self.startFileNumFFT = videoParams['startFileNumFFT']
        self.NumPicFFT = videoParams['NumPicFFT']
 
        if os.path.exists(self.filename):
            self.cap = cv2.VideoCapture(self.filename)
        else:
            sys.exit('Error: No such videofile '+ str(self.filename))

        try:
            if not os.path.exists(self.dirname):
                os.makedirs(self.dirname)
        except OSError:
            print ('Error: Creating directory of data')

#TODO: class with results

        self.timestamps = []
        self.isSuccess = True
        self.areas = []
        self.figFFT = None
        if self.needToShowFFT:
            self.figFFT = analysis.MakeFigureFFT()

    def Run(self):
        print('Processing ' + self.dirname)
        currentFrame = 0
        while(self.isSuccess):
            # Capture frame-by-frame
            self.isSuccess, frame = self.cap.read()
            if not self.isSuccess:
                break

            # Saves image of the current frame in jpg file
            name =  './' + self.dirname + '/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            if self.isSaveFrames:
                cv2.imwrite(name, frame)

            # Process image
            if currentFrame >= self.startFrame and currentFrame < self.finalFrame and currentFrame % self.frameStep == 0:
                #area = pil.CountPixel(frame, False, True)
                pixelCounter, thresholdImg, threshold = binarization.GetPixelsOtsuThreshold(frame,self.xmin, self.xmax, self.ymin, self.ymax)
                contour = binarization.GetContours(thresholdImg, frame, self.needToShowContour, self.xmin, self.ymin)
                analysis.ProcessFrame(contour, self.dirname, currentFrame, self.needToShowFFT, self.MaxFreq, self.figFFT)
                area = pixelCounter*self.pixelToCm*self.pixelToCm
                self.areas.append(area)
                self.timestamps.append(self.cap.get(cv2.CAP_PROP_POS_MSEC))

            currentFrame += 1

        # Save results
        if self.needToSaveAreas:
            with open(self.dirname + '_Areas.txt', 'w') as f:
                for i in range(len(self.areas)):
                    f.write('%s %s \n' %(self.timestamps[i], self.areas[i]))
            plt.plot(self.areas)
            plt.show()

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
    
    def AverageNUFFT(self):
        Fouriers = []
        try:
            for i in range(self.NumPicFFT):
                filename = './' + self.dirname + '/contour'+(str)(self.startFileNumFFT+i) + '.txt'
                print('Process ' + filename)
                data = np.loadtxt(filename)
                Fouriers.append(analysis.ApplyFINUFFT(data, False, self.MaxFreq, None))
        except OSError:
            print ('Error: cannot read contours from .txt files')
        print('Start FFT averaging ...')
        averFourier = np.empty(self.MaxFreq)
        for j in range(self.MaxFreq):
            averFourier[j] = 0
            for i in range(self.NumPicFFT):
                N = len(Fouriers[i])
                averFourier[j] += abs(Fouriers[i][N//2+j])
            averFourier[j] /= self.NumPicFFT
        print('Finish FFT averaging ...')
        np.savetxt(self.dirname + '_AverFFT.txt', averFourier)  
        plt.xlabel('Frequency')
        plt.ylabel('|A|')
        plt.title('Average Fourier Descriptors')
        plt.plot(averFourier)
        plt.savefig(self.dirname + '_AverFFT.png')
        plt.show()
        return 1

