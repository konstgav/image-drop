import cv2
import binarization

img = cv2.imread('./001/frame1000.jpg')
if img is None:
    exit('Image does not exist.')
xmin = 250
xmax = 420
ymin = 80
ymax = 220
pixelCounter, thresholdImg, threshold = binarization.GetPixelsOtsuThreshold(img, xmin, xmax, ymin, ymax)
contours = binarization.GetContours(thresholdImg, img, True, xmin, ymin)
cv2.waitKey(10000)