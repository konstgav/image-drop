import cv2

def GetPixelsOtsuThreshold(img, xmin, xmax, ymin, ymax):
    img = img[ymin:ymax, xmin:xmax]
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retVal, thresholdImg = cv2.threshold(grayImg, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    nonZeroPixelsCount = cv2.countNonZero(thresholdImg)
    return nonZeroPixelsCount, thresholdImg, retVal

def GetContours(thresholdImg, img, needToShow, xmin, ymin):
    contours, hierarchy = cv2.findContours(thresholdImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    maxContour = 0
    maxContourValue = contours[0].shape[0]
    for i in range(1,len(contours)):
        if contours[i].shape[0] > maxContourValue:
            maxContour = i
            maxContourValue = contours[i].shape[0]
    contour = contours[maxContour]
    for p in contour:
        p[0,0] += xmin
        p[0,1] += ymin
    cv2.drawContours(img, contours, maxContour, (255,0,0), 2)
#    cv2.imwrite('test.png', img)
    if needToShow:
        if img.shape[:2][0]>600:
            img = ResizeWithAspectRatio(img, height = 600)
        cv2.imshow('Contours', img)
        cv2.waitKey(1)
    return contour

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)