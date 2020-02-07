from PIL import Image, ImageFilter
from numpy import array, empty
import matplotlib.pyplot as plt
from math import pi, sqrt

def Resize(picOrig, compressCoef = 2):
    widthOrig, heightOrig = picOrig.size
    width = widthOrig//compressCoef
    height = heightOrig//compressCoef
    pic = picOrig.resize((width, height))
    pic.save('redCompressed.JPG')
    return pic

def CountPixel(pic, needGrayShow):
    data = array(pic)
    height = data.shape[0]
    width = data.shape[1]
    pixelCounter = 0
    grayArray = empty([height,width], int)
    threshold = 290
    imin = 101
    imax = 224
    jmin = 273
    jmax = 390
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
    pixelToCm = 5./220
    area = pixelCounter*pixelToCm*pixelToCm
    xCenter = xCenter/pixelCounter
    yCenter = yCenter/pixelCounter
    r = sqrt(pixelCounter/pi)
    return area, xCenter, yCenter, r

#picOrig = Image.open("./images/red-test.jpg")
#redPixelCounter = CountPixel(picOrig)
#print('red Pixel Counter: ', redPixelCounter)
#pixelToCm = 1.4/179
#redArea = redPixelCounter*pixelToCm*pixelToCm
#exactArea = 1.5386
#print('red Area: ', redArea)
#print('exact Area: ', exactArea)
