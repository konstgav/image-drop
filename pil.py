from PIL import Image, ImageFilter
from numpy import array, empty, pi, sqrt
import matplotlib.pyplot as plt
import cv2

def Resize(picOrig, compressCoef = 2):
    widthOrig, heightOrig = picOrig.size
    width = widthOrig//compressCoef
    height = heightOrig//compressCoef
    pic = picOrig.resize((width, height))
    pic.save('redCompressed.JPG')
    return pic

def CountPixel(pic, needGrayShow, needCircleShow):
    data = array(pic)
    height = data.shape[0]
    width = data.shape[1]
    pixelCounter = 0
    grayArray = empty([height,width], int)
    threshold = 290
    imin = 75
    imax = 240
    jmin = 225
    jmax = 440
    xCenter = 0.
    yCenter = 0.
    for i in range(imin,imax+1):
        for j in range(jmin,jmax+1):
            red = data[i,j,0]
            green = data[i,j,1]
            blue = data[i,j,2]
            gray = (int)(red) + (int)(green) + (int)(blue)
            grayArray[i,j] = gray
            if gray < threshold:
                pixelCounter = pixelCounter + 1
                xCenter = xCenter + j
                yCenter = yCenter + i 
    if needGrayShow:
        plt.gray()
        plt.imshow(grayArray[imin:imax+1, jmin:jmax+1])
        plt.show()
    pixelToCm = 6./263
    area = pixelCounter*pixelToCm*pixelToCm

    r = 0
    if pixelCounter > 0:
        xCenter = xCenter/pixelCounter
        yCenter = yCenter/pixelCounter
        r = sqrt(pixelCounter/pi)

    # Displaying the image
    if needCircleShow and r > 0:
        frameCircle = cv2.circle(pic, ((int)(xCenter), (int)(yCenter)), (int)(r), (255, 0, 0), 2) 
        cv2.imshow('Circle', frameCircle)
        cv2.waitKey(1)
                
    return area