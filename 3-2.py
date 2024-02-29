import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/nanosf/Desktop/images/soccer.webp')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

h=cv.calcHist([img],[2],None,[256],[0,256])
plt.plot(h,color='r',linewidth=1)