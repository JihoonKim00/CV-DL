import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/nanosf/Desktop/images/soccer.webp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

t,bin_img = cv.threshold(img[:,:,2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

print('threshold value=',t)

cv.imshow('R channel', img[:,:,2])
cv.imshow('R channel binarization', bin_img)

cv.waitKey()
cv.destroyAllWindows()