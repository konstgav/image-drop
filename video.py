import cv2
import numpy as np
import os
import json 
import pil
import matplotlib.pyplot as plt
import sys
import binarization
import analysis

# Reading video parameters from json file
with open('fractal2.param', 'r')  as json_file:
    videoParams = json.load(json_file)

filename = videoParams['filename']
dirname = videoParams['dirname']
frameStep = videoParams['frameStep']
startFrame = videoParams['startFrame']
finalFrame = videoParams['finalFrame']
isSaveFrames = videoParams['isSaveFrames']
needToShowContour = videoParams['needToShowContour']
xmin = videoParams['xmin']
xmax = videoParams['xmax']
ymin = videoParams['ymin']
ymax = videoParams['ymax']
needToSaveAreas = videoParams['needToSaveAreas']
needToShowFFT = videoParams['needToShowFFT']
MaxFreq = videoParams['MaxFreq']
pixelToCm = videoParams['pixelToCm']
 
# Playing video from file:
if os.path.exists(filename):
    cap = cv2.VideoCapture(filename)
    print('Processing ' + dirname)
else:
    sys.exit('Error: No such file '+ str(filename))

try:
    if not os.path.exists(dirname):
        os.makedirs(dirname)
except OSError:
    print ('Error: Creating directory of data')

#TODO: class with results
#TODO: image processor class
#TODO: tkinter gui

timestamps = []
currentFrame = 0
isSuccess = True
areas = []
figFFT = None
if needToShowFFT:
    figFFT = analysis.MakeFigureFFT()

while(isSuccess):
    # Capture frame-by-frame
    isSuccess, frame = cap.read()
    if not isSuccess:
        break

    # Saves image of the current frame in jpg file
    name =  './' + dirname + '/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    if isSaveFrames:
        cv2.imwrite(name, frame)

    # Process image
    if currentFrame >= startFrame and currentFrame < finalFrame and currentFrame % frameStep == 0:
        #area = pil.CountPixel(frame, False, True)
        pixelCounter, thresholdImg, threshold = binarization.GetPixelsOtsuThreshold(frame, xmin, xmax, ymin, ymax)
        contour = binarization.GetContours(thresholdImg, frame, needToShowContour, xmin, ymin)
        analysis.ProcessFrame(contour, dirname, currentFrame, needToShowFFT, MaxFreq, figFFT)
        area = pixelCounter*pixelToCm*pixelToCm
        areas.append(area)
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))

    currentFrame += 1

# Save results
if needToSaveAreas:
    with open(dirname + 'Areas.txt', 'w') as f:
        for i in range(len(areas)):
            f.write('%s %s \n' %(timestamps[i], areas[i]))
    plt.plot(areas)
    plt.show()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
