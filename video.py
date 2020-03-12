import cv2
import numpy as np
import os
import pil
import matplotlib.pyplot as plt
import sys
import binarization
import analysis

# Playing video from file:
filename = './images/fractal1.MOV'
if os.path.exists(filename):
    cap = cv2.VideoCapture(filename)
else:
    sys.exit('Error: No such file '+ str(filename))

dirname = os.path.splitext(os.path.basename(filename))[0]
print('Processing ' + dirname)

try:
    if not os.path.exists(dirname):
        os.makedirs(dirname)
except OSError:
    print ('Error: Creating directory of data')

#TODO: serialize settings to json on disk
#TODO: class with results
#TODO: image processor class
currentFrame = 0
success = True
areas = []
frameStep = 10
startFrame = 245
finalFrame = 920
isSaveFrames = False
timestamps = []
while(success):
    # Capture frame-by-frame
    success, frame = cap.read()
    if not success:
        break

    # Saves image of the current frame in jpg file
    name =  './' + dirname + '/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    if isSaveFrames:
        cv2.imwrite(name, frame)

    # Process image
    if currentFrame >= startFrame and currentFrame < finalFrame and currentFrame % frameStep ==0:
        #TODO: add roi
        xmin = 1400
        xmax = 2160
        ymin = 640
        ymax = 1500

        #area = pil.CountPixel(frame, False, True)
        pixelCounter, thresholdImg, threshold = binarization.GetPixelsOtsuThreshold(frame, xmin, xmax, ymin, ymax)
        contour = binarization.GetContours(thresholdImg, frame, True, xmin, ymin)
        analysis.ProcessFrame(contour, dirname, currentFrame)
        pixelToCm = 6./263
        area = pixelCounter*pixelToCm*pixelToCm
        areas.append(area)
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))

    currentFrame += 1

# Save results
with open(dirname+'.txt', 'w') as f:
    for i in range(len(areas)):
        f.write('%s %s \n' %(timestamps[i], areas[i]))
plt.plot(areas)
plt.show()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
