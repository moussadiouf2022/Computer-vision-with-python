import cv2 as cv

# simulation choice
Grayscale_image = 0;
Blur_image = 0;
Edge_image = 0;
Dilating_image = 0;
Erroded_image = 0;
Resize_image = 0;
Cropp_image = 1;
    
im = cv.imread(r"C:\Users\hp\opencv_tuturial_python\image_0.jpg")
cv.imshow('Image_1',im)


# Converting to grayscale
if Grayscale_image == 1:
    gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray',gray)

# Blur image 
if Blur_image  == 1:
    blur = cv.GaussianBlur(im, (7,7), cv.BORDER_DEFAULT)
    cv.imshow('Blur',blur)

# Blur image 
if Edge_image == 1:
    canny = cv.Canny(im, 125, 175)
    cv.imshow('Canny Edges',canny)

# Dilating
if Dilating_image == 1:
    dilated = cv.dilate(canny, (7,7),iterations=1)
    cv.imshow('Dilate',dilated)

# Eroding 
if Erroded_image == 1:
    erroded = cv.erode(dilated,(3,3), iterations=1)
    cv.imshow('Erroded',erroded)

# Resize image
if Resize_image == 1:
    resized = cv.resize(im,(500,500),interpolation=cv.INTER_CUBIC)
    cv.imshow('Resized',resized)

# Cropping
if Cropp_image == 1:
    cropped = im[50:500, 200:400]
    cv.imshow('Cropped',cropped)

cv.waitKey(0)