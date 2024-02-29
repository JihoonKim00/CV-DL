import cv2 as cv

img=cv.imread('C:/Users/nanosf/Desktop/images/TEM.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 5,1, param1=150,param2=20,minRadius=1,maxRadius=10)

for i in circles[0]:
    cv.circle(img, (int(i[0]), int(i[1])), int(i[2]),(255,0,0),2)

cv.imshow('img',img)

cv.waitKey()
cv.destroyAllWindows()
