from PIL import Image, ImageFilter
from numpy import array, empty
import matplotlib.pyplot as plt

try:
	picOrig = Image.open("drop.jpg")
except FileNotFoundError:
        print("File not found")

widthOrig, heightOrig = picOrig.size
compressCoef = 2
width = widthOrig//compressCoef
height = heightOrig//compressCoef
pic = picOrig.resize((width, height))
pic.save('redCompressed.JPG')

data = array(pic)

redPixelCounter = 0
grayArray = empty([height,width], int)
threshold = 280
for i in range(height):
    for j in range(width):
        red = data[i,j,0]
        green = data[i,j,1]
        blue = data[i,j,2]
        gray = (int)(red) + (int)(green) + (int)(blue)
        grayArray[i,j] = gray
        if gray < threshold:
            redPixelCounter = redPixelCounter + 1
plt.gray()
plt.imshow(grayArray)
plt.show()

print('red Pixel Counter: ', redPixelCounter)
pixelToCm = 1.4/179
redArea = redPixelCounter*pixelToCm*pixelToCm
exactArea = 1.5386

print('red Area: ', redArea)
print('exact Area: ', exactArea)
