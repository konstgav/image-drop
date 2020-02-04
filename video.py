import cv2
import numpy as np
import os
import pil
import matplotlib.pyplot as plt

# Playing video from file:
filename = './images/drop.mp4'
cap = cv2.VideoCapture(filename)

dirname = os.path.splitext(os.path.basename(filename))[0]
print(dirname)

try:
    if not os.path.exists(dirname):
        os.makedirs(dirname)
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
success = True
pixelNumbers = []
frameStep = 100
startFrame = 138
finalFrame = 5080
isSaveFrames = True
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
        pixelNumber = pil.CountPixel(frame)
        pixelNumbers.append(pixelNumber)

    # To stop duplicate images
    currentFrame += 1

# Save results
with open(dirname+'.txt', 'w') as f:
    for pixelNumber in pixelNumbers:
        f.write("%s\n" % pixelNumber)
plt.plot(pixelNumbers)
plt.show()

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
