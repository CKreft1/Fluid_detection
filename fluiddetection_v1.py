import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("testslide.jpg")
blank=np.zeros(img.shape[:2], dtype="uint8")
blank2=blank.copy()
b,g,r= cv.split(img)
redthreshold, redthresh=cv.threshold(r, 200, 255, cv.THRESH_BINARY)
greenthreshold, greenthresh=cv.threshold(g, 200, 255, cv.THRESH_BINARY)
cv.imshow("image", img)

circles = cv.HoughCircles(greenthresh, cv.HOUGH_GRADIENT,1,20, param1=4,param2=7,minRadius=1,maxRadius=10)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the center of the circle
    # cv.circle(img,(i[0],i[1]),2,(255,0,255),3)
    # draw the outer circle
    if i[2]<=5:
        cv.circle(blank,(i[0],i[1]),(i[2]+3),(255,255,255),-1)
    else:
        cv.circle(blank,(i[0],i[1]),i[2],(255,255,255),-1)
    # cv.circle(img,(i[0],i[1]),2,(0,0,0),3)
mask=cv.bitwise_not(blank)
masked_thresh=cv.bitwise_and(greenthresh, greenthresh, mask=mask)
masked_img=cv.bitwise_and(img, img, mask=mask)

def get_number_of_thresholded_pixels(image):
    x=image.shape[1]
    y=image.shape[0]
    thresholded_pixelnumber=0
    unthresholded_pixelnumber=0
    for i in range(y):
        for l in range(x):
            pixel=image[i,l]
            if pixel==255:
                thresholded_pixelnumber+=1
            else:
                unthresholded_pixelnumber+=1

    return (thresholded_pixelnumber, unthresholded_pixelnumber)
    #run this on a thresholded image to get the number of thresholded and unthresholded pixels

def get_image_area(image):
    x=image.shape[1]
    y=image.shape[0]
    area=x*y
    return area
    #self-explanatory

def calculate_proportion_thresholded(image):
    thresholded=get_number_of_thresholded_pixels(image)[1]
    area=get_image_area(image)
    percent=(thresholded/area)
    return percent
    #combines input from previous functions to give a decimal representing the proportion of thresholded pixels
    #change 1 to 0 to get the number of thresholded pixels, and the 2 outputs should add up to 1.
    #closer to 1 is better
print(calculate_proportion_thresholded(masked_thresh))
cv.imshow("thresh", masked_thresh)
cv.imshow("image", masked_img)





# TODO: figure out how to deal with the rectangles deposited on the sides. Try masking over them (hough transform method?)
# may not be necessary
# TODO: Maybe: set min r=20, max r=20 and fit a masking circle to the center circle using another hough loop. Detect if all the pixels within the mask are green somehow to verify that it's right?
cv.waitKey(0)
