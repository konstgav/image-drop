import cv2
import binarization

img = cv2.imread('./fractal/frame1100.jpg')
if img is None:
    exit('Image does not exist.')
xmin = 690
xmax = 1300
ymin = 230
ymax = 960
pixelCounter, thresholdImg, threshold = binarization.GetPixelsOtsuThreshold(img, xmin, xmax, ymin, ymax)
contours = binarization.GetContours(thresholdImg, img, True, xmin, ymin)
cv2.waitKey(10000)