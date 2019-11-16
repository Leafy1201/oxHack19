import numpy as np
import cv2 as cv

imo = cv.imread('./Test Data/Screenshot_20191116_151213.png')
img = cv.cvtColor(imo, cv.COLOR_BGR2GRAY)
(thresh, imb) = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

def rescale_frame(frame, wpercent=50, hpercent=50):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)


#cv2.imshow('Original image',originalImage)
#cv2.imshow('Gray image', grayImage)

ret, thresh = cv.threshold(imb, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv.findContours(thresh, 1, 2)
contours = contours[1:]
hierarchy = hierarchy[0][1:]
cv.drawContours(imo, contours, -1, (0,255,0), 1)

print(hierarchy)

for a in range(0,len(contours)):
    if hierarchy[a][3] != 0:
        pass
    else:
        cnt  = contours[a]
        x,y,w,h = cv.boundingRect(cnt)
        if a%3 == 0:
            colour = (255,0,0)
        elif a%3 == 1:
            colour = (0,255,0)
        elif a%3 == 2:
            colour = (0,0,255)
        M = cv.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.circle(imo, (cx, cy), 4, (255, 0, 255),-1)
        cv.rectangle(imo,(x,y),(x+w,y+h),colour,1)

cv.imshow("recog", rescale_frame(imo))
  
cv.waitKey(0)
cv.destroyAllWindows()
