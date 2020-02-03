import cv2
import numpy as np
import os

# Playing video from file:
filename = 'drop.mp4'
cap = cv2.VideoCapture(filename)

# TODO:изменить имя каталога
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
success = True
while(success):
    # Capture frame-by-frame
    success, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()