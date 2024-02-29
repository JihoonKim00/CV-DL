import cv2 as cv
import sys

img = cv.imread('C:/Users/nanosf/Desktop/images/soccer.webp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.imshow('original_RGB', img)
cv.imshow('Upper left half', img[0:img.shape[0]//4*3, 0:img.shape[1]//2,:])

cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel',img[:,:,1])
cv.imshow('B channel',img[:,:,0])


cv.waitKey()
cv.destroyAllWindows()