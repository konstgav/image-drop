import cv2
import numpy as np
import os
import pil
import matplotlib.pyplot as plt

# Playing video from file:
filename = './images/003.mp4'
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
areas = []
frameStep = 20
startFrame = 100
finalFrame = 1000000
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
        area, xCenter, yCenter, radius = pil.CountPixel(frame, False)
        areas.append(area)
        
        # Displaying the image
        if radius > 0:
            frameCircle = cv2.circle(frame, ((int)(xCenter), (int)(yCenter)), (int)(radius), (255, 0, 0), 2) 
            cv2.imshow('Circle', frameCircle)
            cv2.waitKey(1) 
        
    # To stop duplicate images
    currentFrame += 1

# Save results
with open(dirname+'.txt', 'w') as f:
    for area in areas:
        f.write("%s\n" % area)
plt.plot(areas)
plt.show()

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
